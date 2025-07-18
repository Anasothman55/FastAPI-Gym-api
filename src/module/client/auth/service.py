from datetime import  timedelta
from fastapi import HTTPException, status

from rich import print
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.config.security.email_token import create_url_safe_token, decode_url_safe_token
from src.config.security.hashing import password_hash, password_decode
from src.config.setting import settings
from src.database.redis.taskq import send_cre
from src.database.sql.model import ClientModel, UserModel, EmailRegisterModel, VerificationTokenModel
from src.module.client.auth.helper import verify_token_helper
from src.module.client.auth.schema.body import ClientAuthRegister, ClientAuthLogin

from src.module.client.client.service import create_client, get_one_client
from src.shared.timestemp import get_timestamp


async def email_register_service(db: AsyncSession, body: ClientAuthRegister) -> dict[str, str]:
  """ Client email register service """
  result = await create_client(
    db,
    user= UserModel(hash_password = password_hash(body.password), language = body.language),
    email= EmailRegisterModel(email = body.email),
    client= ClientModel(name = body.name)
  )
  email = result.email.email

  verify_token = create_url_safe_token({'email': email})

  token = VerificationTokenModel(
    token = verify_token,
    expires_at = get_timestamp() + timedelta(hours=settings.EMAIL_EXP_HOUR),
    email_register_id = result.email.id
  )

  db.add(token)
  await db.commit()

  send_cre.delay(email, result.client.name, verify_token )

  return {
    'msg': 'We send an verification email to your email address please verify your email'
  }


async def verify_email_service(db: AsyncSession, token: str)-> EmailRegisterModel:
  async with db.begin():
    token_obj = await verify_token_helper(db, token)
    email = token_obj.Email

    await db.flush()

    token_obj.used = True
    email.set_verified()

  await db.commit()
  await db.refresh(token_obj)
  await db.refresh(email)

  print(email)
  return email


async def login_email_service(
    db: AsyncSession,
    body: ClientAuthLogin
):
  stmt = select(EmailRegisterModel).where(EmailRegisterModel.email == body.email)
  result = await db.execute(stmt)
  obj = result.scalar_one_or_none()

  if not obj:
    raise HTTPException(status.HTTP_400_BAD_REQUEST, 'No email found')

  password_decode(obj.Users.hash_password, body.password)

  return await get_one_client(db,'Email', obj)























