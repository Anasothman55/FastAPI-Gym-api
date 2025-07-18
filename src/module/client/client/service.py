from typing import Union, TypedDict, Any
from rich import print
from sqlalchemy import select, or_, and_
from sqlalchemy.orm import selectinload
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.shared.enums.constant import StatusEnum, UserRole
from .schema import ClientCreateTypeResponse
from src.database.sql.model import UserModel, EmailRegisterModel, ClientModel, Base
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




async def get_one_client(
    db: AsyncSession,
    field: str,
    value: Any,
    model_status: StatusEnum = StatusEnum.ACTIVE,
    deleted: bool = False
):

  stmt = (
    select(UserModel)
    .options(
      selectinload(UserModel.Email).selectinload(EmailRegisterModel.VerificationToken),
      selectinload(UserModel.Cities),
      selectinload(UserModel.Phone),
      selectinload(UserModel.Google),
      selectinload(UserModel.Client)
    )
    .where(
      and_(
        UserModel.role == UserRole.CLIENT,
        getattr(UserModel, field) == value,
        UserModel.status == model_status,
      )
    )
  )

  if not deleted:
    stmt = stmt.where(UserModel.delete_at == None)

  result = await db.execute(stmt)
  return  result.scalar_one_or_none()





