from sqlalchemy import Integer, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .users import User


class Profile(Base):
    __tablename__ = "users_profile"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True) 
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.user_id"), unique=True, nullable=False)
    challenges_solved: Mapped[int] = mapped_column(Integer, unique=False, nullable=False)
    katas_solved: Mapped[int] = mapped_column(Integer, unique=False, nullable=False)
    created_at: Mapped[str] = mapped_column(String, unique=False, nullable=True)

    user: Mapped["User"] = relationship("User", back_populates="profile")
