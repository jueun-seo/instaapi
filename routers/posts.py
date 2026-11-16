from datetime import datetime

from fastapi import APIRouter
from pydantic import BaseModel, ConfigDict
from sqlalchemy import select

from deps import SessionDep
from models import Post
from schemas import PostOut

router = APIRouter(prefix='/api/posts')


class PostOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    content: str
    created_at: datetime
    user: int


@router.get('', response_model=list[PostOut])
def post_list(db: SessionDep):
    posts = db.scalars(select(Post).order_by(Post.created_at.desc())).all()

    # for post in posts:
    #     print(post.user.username)
    
    return posts
