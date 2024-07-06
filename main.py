from fastapi import FastAPI

app = FastAPI(
    title="Events API",
    version="0.1.0"
)

@app.get("/healthcheck")
def healthcheck() -> dict:
    return {"msg": "server is up!"}