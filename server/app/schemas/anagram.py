from pydantic import BaseModel
from datetime import datetime

#added the sorted here for nested output purposes
class AnagramSortedKeyNested(BaseModel):
    id: int
    sorted_anagram: str

    class Config:
        from_attributes = True

class AnagramBase(BaseModel):
    word: str


class AnagramCreate(AnagramBase):
    pass


class AnagramRead(AnagramBase):
    id: int
    sorted_key_id: int
    created_at: datetime

    class Config:
        from_attributes = True


