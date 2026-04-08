from sqlalchemy.orm import Session
from repositories import anagram_entry_repository, anagram_sorted_key_repository
from clients import dictionary_client

def build_sorted_key(word: str) -> str:
    return "".join(sorted(word.lower().strip()))

def check_word_valid(word: str) -> bool:
    return dictionary_client.is_valid_word(word)


def get_or_create_sorted_key(db: Session, word: str):
    sorted_word = build_sorted_key(word)

    key_existing = anagram_sorted_key_repository.get_by_sorted_anagram(db, sorted_word)
    if key_existing is None:
        #checking here if the word exist so we won't insert a sorted key for a word that's not even valid
        valid_word = check_word_valid(word)
        if valid_word:
            key_existing = anagram_sorted_key_repository.create(db, sorted_word)
        
    return key_existing

def create_entry(db: Session, word: str):
    
    key_existing_or_word_valid = get_or_create_sorted_key(db, word)

    if key_existing_or_word_valid is None:
        raise ValueError("Word not found in dictionary")
    else:
        key_id = key_existing_or_word_valid.id

    return anagram_entry_repository.create(db, word, key_id)

def get_anagrams_for_word(db: Session, word: str):
    sorted_word = build_sorted_key(word)
    key = anagram_sorted_key_repository.get_by_sorted_anagram(db, sorted_word)

    if key is None:
        return []
    
    return anagram_entry_repository.list_by_sorted_key_id(db, key.id)
    
