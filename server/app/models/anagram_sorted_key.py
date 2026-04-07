from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.session import Base

class AnagramSortedKey(Base):
    __tablename__ = "anagram_sorted_key"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    sorted_anagram: Mapped[str] = mapped_column(String(45), unique=True)

    #reverse relationship
    entries = relationship("AnagramEntries", back_populates="sorted_key")