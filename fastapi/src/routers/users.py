from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas, auth
from ..auth import get_current_user
from ..dependencies import get_db
from ..models import User
from ..schemas import UserRead
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()


@router.post("/register", response_model=schemas.Token)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = auth.get_user(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    token = auth.create_access_token(data={"sub": db_user.username})
    return {"access_token": token, "token_type": "bearer"}


@router.post("/token", response_model=schemas.Token)
def login(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db)
):
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    token = auth.create_access_token(data={"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}


@router.get("/users/me/", response_model=UserRead)
def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user
