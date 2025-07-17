from typing import Union, TypedDict

from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from .schema import ClientCreateTypeResponse
from src.database.sql.model import UserModel, EmailRegisterModel, ClientModel
from fastapi import status , HTTPException



async def create_client(
    db: AsyncSession,
    user: UserModel,
    client: ClientModel,
    email: EmailRegisterModel
) -> ClientCreateTypeResponse :
  try:
    async with db.begin():
      db.add(user)
      await db.flush()

      email.user_uid = user.uid
      db.add(email)

      client.user_uid = user.uid
      db.add(client)

    await db.refresh(user)
    return ClientCreateTypeResponse(user= user,client= client,email= email)

  except IntegrityError as ex:
    error_str = str(ex.orig)
    sc = status.HTTP_400_BAD_REQUEST
    if any(err in error_str for err in ["UniqueViolationError", "ExclusionViolationError", "PrimaryKeyViolationError"]):
      sc = status.HTTP_409_CONFLICT

    raise HTTPException(
      status_code= sc,
      detail=  str(ex.orig).split(':')[2].strip()
    )






