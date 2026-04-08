from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.session import get_db
from schemas.anagram import AnagramCreate, AnagramRead
from services.anagram_service import create_entry, get_anagrams_for_word

router = APIRouter()

@router.post("/", response_model=AnagramRead)
def create_anagram(payload: AnagramCreate, db: Session = Depends(get_db)):
    return create_entry(db, payload.word)

@router.get("/{word}", response_model=AnagramRead)
def get_anagrams(word: str, db: Session = Depends(get_db)):
    return get_anagrams_for_word(db, word)
