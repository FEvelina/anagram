from sqlalchemy import String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.session import Base
from datetime import datetime

class AnagramEntries(Base):
    __tablename__ = "anagram_entrie"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    word: Mapped[str] = mapped_column(String(45), unique=True)
    #fk
    sorted_key_id: Mapped[int] = mapped_column(
        ForeignKey("anagram_sorted_key.id")
        )
    created_at: Mapped[datetime] = mapped_column(DateTime)
    encountered: Mapped[int] = mapped_column(Integer)

    #reverse relationship
    sorted_key = relationship("AnagramSortedKey")