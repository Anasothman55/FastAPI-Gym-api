from datetime import datetime, timedelta, timezone
from sqlalchemy.ext.asyncio import AsyncSession

from src.config.security.email_token import create_url_safe_token
from src.config.security.hashing import password_hash
from src.config.setting import settings
from src.database.redis.taskq import send_cre
from src.database.sql.model import ClientModel, UserModel, EmailRegisterModel, VerificationTokenModel
from src.module.client.auth.schema import ClientAuthRegister


from src.module.client.client.service import create_client


async def email_register_service(db: AsyncSession, body: ClientAuthRegister) -> UserModel:
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
    expires_at = datetime.now(timezone.utc) + timedelta(hours=settings.EMAIL_EXP_HOUR),
    email_register_id = result.email.id
  )

  db.add(token)
  await db.commit()

  send_cre.delay(email, result.client.name, verify_token )

  return result.user


async def verify_email_service(token: str):
  pass









