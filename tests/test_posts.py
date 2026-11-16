from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_post_list():
  res = client.get('/api/posts')
  assert res.status_code == 200


def test_post_detail_404():
  res = client.get('/api/posts/9999999')
  assert res.status_code == 404
  assert res.json() == {'detail': "해당 게시물이 없습니다."}


def test_post_create_empty_422():
  res = client.post('/api/posts', json={'content': '', 'user_id': 1})
  assert res.status_code == 422


def test_post_create_and_delete():
  res = client.post('/api/posts', json={'content': 'hello', 'user_id': 1})
  assert res.status_code == 201
  post_id = res.json()['id']

  res = client.delete(f'/api/posts/{post_id}')
  assert res.status_code == 204
  assert client.get(f'/api/posts/{post_id}').status_code == 404
