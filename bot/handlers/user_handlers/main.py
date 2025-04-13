from loguru import logger
from aiogram import Router, types, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter, Command
from database.telegram_db_methods.db_methods import DBMethods

from states.user_states import UserStates

from utils.answer_keyboards import invite_variants, kata_variants, data_variants

from api_data.parse_request import get_codewars_user

from templates import render_template


logger.remove()
logger.add(
    sink=lambda msg: print(msg, end=""),
    format="<level>[{time:YYYY-MM-DD HH:mm:ss}] #{level:<8} {file.name}:"
           "{line} - {name} - {message}</level>",
    level="DEBUG",
    colorize=True
)


user_main_router = Router()


@user_main_router.message(Command("getme"), StateFilter(UserStates.global_state))
async def start(message: types.Message, state: FSMContext):
    user_id = message.from_user.id

    db_methods = DBMethods()

    user, profile = await db_methods.get_user_data(user_id)

    if user and profile:
        data = {
            "name": message.from_user.full_name,
            "username": user.user_username,
            "challenges_solved": profile.challenges_solved,
            "katas_solved": profile.katas_solved,
            "created_at": profile.created_at,
        }
    else:
        data = {
            "name": message.from_user.full_name,
            "username": "Unknown",
            "challenges_solved": 0,
            "katas_solved": 0,
            "created_at": "N/A",
        }

    await message.answer(render_template("profile.html", values=data))


@user_main_router.message(F.text, StateFilter(UserStates.get_id))
async def start(message: types.Message, state: FSMContext):
    await state.update_data(user_id = message.text)
    await state.set_state(UserStates.get_codewars_profile)
    await message.answer(render_template("challenge_start_codewars.html"))


@user_main_router.message(F.text, StateFilter(UserStates.get_codewars_profile))
async def start(message: types.Message, state: FSMContext):    
    await state.update_data(codewars_id = message.text)
    res = get_codewars_user(message.text)
    if res == True:
        await message.answer(render_template("challenge_done.html"), reply_markup=kata_variants())
        await state.set_state(UserStates.get_katas_amount)
    else:
        await message.answer("Invalid username or codewars api is not responding! Try again!")



@user_main_router.message(Command("challenge"), StateFilter(UserStates.global_state))
async def challenge(message: types.Message, state: FSMContext):
    await message.answer(render_template("challenge_start.html"), reply_markup=invite_variants())


@user_main_router.callback_query(F.data == 'invite_by_username_callback', StateFilter(UserStates.global_state))
async def invite_by_username_callback(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Write user's id:")
    await state.set_state(UserStates.get_id)


@user_main_router.callback_query(F.data == '1_kata_solve', StateFilter(UserStates.get_katas_amount))
async def handle_katas_amount(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(render_template("challenge_get_time.html"), reply_markup=data_variants())
    await state.set_state(UserStates.get_dates)


@user_main_router.callback_query(F.data == '1_day', StateFilter(UserStates.get_dates))
async def handle_challenge_date(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(render_template("challenge_created.html"))
    await state.set_state(UserStates.global_state)