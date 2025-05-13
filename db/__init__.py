from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.base import Base
from config import DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
