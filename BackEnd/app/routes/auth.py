from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login(username: str, password: str):
    # TODO: check user in DB
    return {"message": "Login success (mock)"}

@router.post("/register")
def register(username: str, password: str):
    # TODO: insert user into DB
    return {"message": "Register success (mock)"}
