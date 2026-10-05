from fastapi import APIRouter, status, Depends, HTTPException
from app.schemas.users import (
    CreateUserResponse,
    CreateUser,
    LoginUser,
    LoginUserResponse,
)
from app.db.db_connections import get_db
from sqlalchemy.orm import Session
from app.db.users_table import User
from app.encryption.encryption import hash_password, check_hash
from app.encryption.jwt import create_access_token, verify_token, restrict_routes

auth_router = APIRouter(tags=["SIGNUP AND SIGNIN"])


# SIGNUPs
@auth_router.post(
    "/signup", status_code=status.HTTP_201_CREATED, response_model=CreateUserResponse
)
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    user_db = db.query(User).filter(User.email == user.email).first()
    if user_db:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="USER ALREADY EXISTS"
        )
    hashed_pw = hash_password(user.password)
    new_user = User(player_name=user.player_name, email=user.email, password=hashed_pw)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return CreateUserResponse(player_name=new_user.player_name)


# SIGNIN


@auth_router.post(
    "/login", status_code=status.HTTP_200_OK, response_model=LoginUserResponse
)
def login(user: LoginUser, db: Session = Depends(get_db)):
    user_db = db.query(User).filter(User.email == user.email).first()
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="WRONG EMAIL OR PASSWORD"
        )
    is_password_matching = check_hash(user.password, user_db.password)
    if not is_password_matching:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="WRONG EMAIL OR PASSWORD"
        )
    access_token = create_access_token({"id": str(user_db.id)})
    return LoginUserResponse(
        player_name=user_db.player_name,
        email=user_db.email,
        access_token=access_token,
        token_type="bearer",
    )
