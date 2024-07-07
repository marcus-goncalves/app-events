from dotenv import load_dotenv
from fastapi import FastAPI
from handlers.users import users
from services import database

load_dotenv()

engine = database.start_engine()
database.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Events API",
    version="0.1.0"
)

@app.get("/healthcheck")
def healthcheck() -> dict:
    return {"msg": "server is up!"}

app.include_router(users)