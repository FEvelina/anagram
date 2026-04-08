from datetime import datetime
from sqlalchemy.orm import Session
from server.app.models.anagram_entry import AnagramEntry

def get_by_word(db: Session, word: str) -> AnagramEntry | None:
    return db.query(AnagramEntry).filter(AnagramEntry.word == word).first()

def create(db: Session, word: str, sorted_key_id: int) -> AnagramEntry:
    entry = AnagramEntry(
        word=word,
        sorted_key_id=sorted_key_id,
        create_at=datetime.now(),
        encountered=1
    )

    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry

#continue the queries for this repository, the key and the user ones
#implement the services and the routes for all of them
#also need the frontend (ugly but meh)