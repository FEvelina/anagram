from sqlalchemy import String, Date, Integer
from sqlalchemy.orm import Mapped, mapped_column
from database.session import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(20), unique=True)
    points: Mapped[int] = mapped_column(Integer)