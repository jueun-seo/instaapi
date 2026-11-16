from fastapi import APIRouter, HTTPException, Depends
from schemas import UserCreate, UserOut
from deps import SessionDep, create_access_token
from models import User
from sqlalchemy import select 
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

router = APIRouter(prefix='/api/auth', tags=['auth'])

@router.post('/signup', response_model=UserOut)
def signup(data: UserCreate, db: SessionDep):
    user = db.scalar(select(User).where(User.username == data.username)) #db에서 조회

    if user:
        raise HTTPException(status_code=409, detail='사용중인 아이디입니다.') #user존재시 강제 에러발생, fastapi에들어있음
    #409 : 니가 요청 보낸건 맞아. 근데 무슨 충돌이 일어나고 있어
    
hashed_pw = password_hash.hash(data.password) #암호화된 비번
User(username=data.uwername, password_hash=hashed_pw)
db.add(user)
db.commit()

return user

@router.post('/login', response_model=Token)
def login(form: Annotated[OAuth2PasswordRequestForm, Depends()] db: SessionDep):
    user = db.scalar(select(User).where(User.username == form.username))

    # 유저가 없거나 비밀번호가 일치하지 않는다면
    if user is None or password_hash.verify(form.password, user.password_hash) 
      raise HTTPException(status_code=401, detail='아이디 또는 비밀번호가 틀렸습니다')

token =create_access_token(user.id)

return {'access_token': token, 'token_type': 'bearer'}