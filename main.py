from typing import Annotated

from fastapi import FastAPI, Path

import database

app = FastAPI()

@app.get("/word-length/{word}", tags=["words"])
async def word_length(word: Annotated[str, Path(title="The word the length of which to return")]):
    return len(word)

@app.get("/health", tags=["lifecycle"])
async def health():
    return database.is_alive()