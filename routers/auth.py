from fastapi import APIRouter, HTTPException, Depends
from schemas import UserCreate, UserOut, Token
from deps import SessionDep, password_hash, create_access_token, CurrentUserDep
from models import User
from sqlalchemy import select
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

router = APIRouter(prefix='/api/auth', tags=['auth'])

@router.post('/signup', response_model=UserOut)
@router.post('/signup', response_model=UserOut, status_code=201)
def signup(data: UserCreate, db: SessionDep):
  user = db.scalar(select(User).where(User.username == data.username))
