from fastapi import FastAPI
from routes.users import users

app = FastAPI(
    title="Events API",
    version="0.1.0"
)

@app.get("/healthcheck")
def healthcheck() -> dict:
    return {"msg": "server is up!"}

app.include_router(users)