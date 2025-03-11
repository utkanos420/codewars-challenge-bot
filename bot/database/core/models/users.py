from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .users_profile import Profile


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True) 
    user_id: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    user_username: Mapped[str] = mapped_column(String, unique=False, nullable=False)

    profile: Mapped["Profile"] = relationship("Profile", back_populates="user", uselist=False)
