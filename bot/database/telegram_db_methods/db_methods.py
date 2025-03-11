from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from database.core.models import User, Profile
from database.core.models import db_helper

class DBMethods:
    def __init__(self):
        self.session = db_helper.get_scoped_session()

    async def get_user(self, user_id: int) -> User | None:
        async with self.session() as session:
            result = await session.execute(select(User).filter_by(user_id=user_id))
            return result.scalars().first()

    async def create_user(self, user_id: int, username: str) -> User:
        async with self.session() as session:
            user = User(user_id=user_id, user_username=username)
            session.add(user)
            await session.commit()
            return user

    async def create_profile(self, user_id: int, challenges_solved: int, katas_solved: int) -> Profile:
        async with self.session() as session:
            profile = Profile(user_id=user_id, challenges_solved=challenges_solved, katas_solved=katas_solved)
            session.add(profile)
            await session.commit()
            return profile

    async def get_profile(self, user_id: int) -> Profile | None:
        async with self.session() as session:
            result = await session.execute(select(Profile).filter_by(user_id=user_id))
            return result.scalars().first()
