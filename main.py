from typing import Annotated

from fastapi import FastAPI, Path, Query

import database

app = FastAPI()

@app.get("/word-length/{word}", tags=["words"])
async def word_length(word: Annotated[str, Path(title="The word the length of which to return")]):
    return len(word)

@app.get("/health", tags=["lifecycle"])
async def health():
    return await database.is_alive()

@app.get("/echo-from-db", tags=["query-test"])
async def echo(number: Annotated[int, Query(title="number to echo from db")]):
    return await database.echo_number(number)