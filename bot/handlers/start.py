from loguru import logger
from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from database.telegram_db_methods.db_methods import DBMethods


logger.remove()
logger.add(
    sink=lambda msg: print(msg, end=""),
    format="<level>[{time:YYYY-MM-DD HH:mm:ss}] #{level:<8} {file.name}:"
           "{line} - {name} - {message}</level>",
    level="DEBUG",
    colorize=True
)


"""
class UserInternalIdMiddleware(BaseMiddleware):
    def get_internal_id(self, user_id: int) -> int:
        return randint(100_000_000, 900_000_000) + user_id

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        user = data["event_from_user"]
        data["internal_id"] = self.get_internal_id(user.id)
        logger.debug("Middleware is here!")
        return await handler(event, data)"
start_router.message.middleware(UserInternalIdMiddleware())
"""


start_router = Router()

@start_router.message(CommandStart())
async def start(message: types.Message, state: FSMContext):

    db = DBMethods()

    user = await db.create_user(user_id=message.from_user.id, username=message.from_user.username)
    logger.debug(f"Created user with credits {message.from_user.id} {message.from_user.username}")

    await message.answer("Hello world from bot!")