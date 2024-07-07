import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def start_engine():
    uri: str = os.getenv("DATABASE_URL")

    engine = create_engine(
        url=uri,
        connect_args={
            "check_same_thread": False
        }
    )
    return engine

LOCAL_SESSION = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=start_engine()
)

def get_session():
    db = LOCAL_SESSION()
    try:
        yield db
    finally:
        db.close()