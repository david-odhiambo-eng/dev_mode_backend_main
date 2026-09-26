from jose import jwt, JWTError
from settings.load_env import SECRET_KEY, ALGORITHM
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException, status, Request, Depends
from app.db.db_connections import get_db
from sqlalchemy.orm import Session
from app.db.tables import User


# creating access token
def create_access_token(data: dict):
    to_encode = data.copy()
    expiry_time = datetime.now(timezone.utc) + timedelta(days=30)
    to_encode.update({"exp": expiry_time})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return encoded_jwt


# verifying access token
def verify_token(token: str):
    jwt_error = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="YOU ARE UNAUTHORIZED"
    )
    try:
        jwt_token = jwt.decode(token, SECRET_KEY, ALGORITHM)
        id = jwt_token.get("id")
        if id == None:
            raise jwt_error
        return id
    except JWTError:
        raise jwt_error


# restricting routes
def restrict_routes(request: Request, db: Session = Depends(get_db)):
    unauthorized_error = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="UNAUTHORIZED"
    )
    header = request.headers.get("Authorization")
    if not header:
        raise unauthorized_error
    parts = header.split()
    if len(parts) != 2:
        raise unauthorized_error
    bearer, token = parts
    if bearer.lower() != "bearer":
        raise unauthorized_error
    id = verify_token(token=token)
    user_db = db.query(User).filter(User.id == id).first()
    if not user_db:
        raise unauthorized_error
    return user_db
