from fastapi import APIRouter, HTTPException
from schemas import UserCreate, UserOut
from deps import SessionDep
from models import User
from sqlalchemy import select 

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
