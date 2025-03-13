from loguru import logger
from datetime import datetime
from typing import Callable, Any, Awaitable, Dict
from random import randint
from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import TelegramObject
from aiogram.filters import StateFilter
from aiogram import BaseMiddleware

from database.telegram_db_methods.db_methods import DBMethods
from states.user_states import UserStates


logger.remove()
logger.add(
    sink=lambda msg: print(msg, end=""),
    format="<level>[{time:YYYY-MM-DD HH:mm:ss}] #{level:<8} {file.name}:"
           "{line} - {name} - {message}</level>",
    level="DEBUG",
    colorize=True
)


class UserInternalIdMiddleware(BaseMiddleware):
    def __init__(self):
        self.db_methods = DBMethods()

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        user = data.get("event_from_user")
        if user:
            user_id = user.id
            username = user.username

            existing_user = await self.db_methods.get_user(user_id)

            if not existing_user:
                logger.debug(f"User {user_id} not found, creating a new user.")
                created_user = await self.db_methods.create_user(user_id, username)
                logger.debug(f"User {user_id} created.")

                created_at = datetime.now().strftime("%d/%m/%Y")

                await self.db_methods.create_profile(
                    user_id=created_user.user_id,
                    challenges_solved=0,
                    katas_solved=0,
                    created_at=created_at
                )
                logger.debug(f"Profile for user {user_id} created.")
            
            data["user_id"] = user_id
            data["user_username"] = username
            logger.debug("Middleware has processed the user.")
        else:
            logger.warning("No user information found in the event data.")
        
        return await handler(event, data)


start_router = Router()
start_router.message.middleware(UserInternalIdMiddleware())


@start_router.message(CommandStart(), StateFilter(None))
async def start(message: types.Message, state: FSMContext):

    logger.debug(f"Created user with credits {message.from_user.id} {message.from_user.username}")

    await message.answer("Hello world from bot!")

    await state.set_state(UserStates.global_state)