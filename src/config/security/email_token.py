
from itsdangerous import URLSafeTimedSerializer
from itsdangerous.exc import BadData
from fastapi import HTTPException, Response, status
from rich import print
from src.config.setting import settings

#? create url safe token with itsdangerous library
serializer = URLSafeTimedSerializer(
  secret_key= settings.EMAIL_VERIFY_SECRET,
  salt= settings.EMAIL_VERIFY_SALT
)

def create_url_safe_token(data: dict[str: str]):
  return serializer.dumps(data)

def decode_url_safe_token(token: str)-> dict:
  try:
    return serializer.loads(token, max_age=settings.EMAIL_EXP_HOUR * 3600 )
  except BadData as ex:
    print(ex.__dict__)
    raise HTTPException(
      status_code= status.HTTP_401_UNAUTHORIZED,
      detail= str(ex.message)
    )

















