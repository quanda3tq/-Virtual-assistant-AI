from sqlalchemy import Column, Integer, String
from app.services.postgres_service import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False, index=True)
    password_hash = Column(String(12), nullable=False)
    gender = Column(String(10), nullable=True)
    birth_year = Column(Integer, nullable=True)