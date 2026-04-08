from sqlalchemy.orm import Session
from models.anagram_sorted_key import AnagramSortedKey

def get_by_sorted_anagram(db: Session, sorted_anagram: str) -> AnagramSortedKey | None:
    return (
        db.query(AnagramSortedKey)
        .filter(AnagramSortedKey.sorted_anagram == sorted_anagram)
        .first()
    )

def create(db: Session, sorted_anagram: str) -> AnagramSortedKey:
    entry = AnagramSortedKey(
        sorted_anagram=sorted_anagram
    )

    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry