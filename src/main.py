from fastapi import FastAPI
from src.routers import movies


app = FastAPI()


@app.get("/")
async def root():
    return { "message": "Приложение работает" }


app.include_router(movies.router)
