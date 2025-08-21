from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/auth", tags=["Auth"])

# Fake DB tạm
fake_users = {}

class User(BaseModel):
    username: str
    password: str

@router.post("/register")
def register(user: User):
    if user.username in fake_users:
        raise HTTPException(status_code=400, detail="User already exists")
    fake_users[user.username] = user.password
    return {"msg": "User registered successfully"}

@router.post("/login")
def login(user: User):
    if fake_users.get(user.username) != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"msg": f"Welcome {user.username}!"}
