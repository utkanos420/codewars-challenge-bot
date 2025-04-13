from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, StateFilter


class UserStates(StatesGroup):
    global_state = State()
    get_id = State()
    get_codewars_profile = State()
    get_katas_amount = State()
    get_dates = State()