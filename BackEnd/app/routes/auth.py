from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.services.postgres_service import get_db
from app.models.user_model import User
import bcrypt

router = APIRouter(prefix="/auth", tags=["Auth"])

# ====== Schemas ======
class UserRegister(BaseModel):
    username: str
    password: str
    gender: str | None = None
    birth_year: int | None = None

class UserLogin(BaseModel):
    username: str
    password: str


# ====== Register ======
@router.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists")

    # Hash password
    hashed_pw = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt())

    new_user = User(
        username=user.username,
        password_hash=hashed_pw.decode("utf-8"),
        gender=user.gender,
        birth_year=user.birth_year
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered successfully", "user_id": new_user.user_id}

# ====== Login ======
@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid username or password")

    # Check password
    if not bcrypt.checkpw(user.password.encode("utf-8"), db_user.password_hash.encode("utf-8")):
        raise HTTPException(status_code=400, detail="Invalid username or password")

    return {"message": "Login successful", "user_id": db_user.user_id}

