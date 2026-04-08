from fastapi import APIRouter

from routes import anagram

api_router = APIRouter()

api_router.include_router(anagram.router, prefix="/anagrams", tags=["anagrams"])