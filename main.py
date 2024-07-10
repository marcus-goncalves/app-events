from dotenv import load_dotenv
from fastapi import FastAPI
from handlers.users import users
from handlers.roles import roles
from handlers.work_shifts import work_shifts
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
app.include_router(roles)
app.include_router(work_shifts)