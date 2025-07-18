from fastapi import HTTPException , status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from src.config.security.email_token import decode_url_safe_token
from src.database.sql.model import  VerificationTokenModel
from src.shared.timestemp import get_timestamp


async def verify_token_helper(db: AsyncSession, token: str)-> VerificationTokenModel:
  decoded = decode_url_safe_token(token)

  stmt =(
    select(VerificationTokenModel)
      .options(selectinload(VerificationTokenModel.Email))
      .where(VerificationTokenModel.token == token)
  )
  result = await db.execute(stmt)
  token_obj: VerificationTokenModel  = result.scalar_one_or_none()

  if not token_obj or token_obj.used:
    raise HTTPException(status.HTTP_400_BAD_REQUEST,'Invalid or already used token')
  if token_obj.expires_at < get_timestamp():
    raise HTTPException(status.HTTP_400_BAD_REQUEST, 'Token expired')
  if token_obj.Email is None or token_obj.Email.email != decoded.get('email'):
    raise HTTPException(status.HTTP_400_BAD_REQUEST, 'Token-email mismatch')

  return token_obj




