from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True) 
    user_id: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    user_username: Mapped[str] = mapped_column(String, unique=False, nullable=False)
