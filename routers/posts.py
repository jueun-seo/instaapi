from fastapi import APIRouter
from deps import SessionDep, PostDep
from sqlalchemy import select
from models import Post
from schemas import PostOut, PostCreate

router = APIRouter(prefix='/api/posts')

@router.get('', response_model=list[PostOut])
def post_list(db: SessionDep):
  posts = db.scalars(select(Post).order_by(Post.created_at.desc())).all()

  # for post in posts:
  #   print(post.user.username)

  return posts


@router.get('/{post_id}', response_model=PostOut)
def post_detail(post: PostDep):
  # post = db.get(Post, post_id)
  return post

@router.post('', response_model=PostOut, status_code=201)
def post_create(data: PostCreate, db: SessionDep):
  post = Post(content=data.content, user_id=data.user_id)
  db.add(post) 
  db.commit()
  return post