from loguru import logger
from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter, Command
from database.telegram_db_methods.db_methods import DBMethods

from states.user_states import UserStates

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

    # Получаем данные пользователя и его профиля
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


