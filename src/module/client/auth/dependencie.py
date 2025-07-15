from typing import Annotated
from sqlalchemy.ext.asyncio import  AsyncSession
from fastapi import  Form
from src.module.client.auth.schema import ClientAuthRegister
from src.shared.dependencies.db import get_db
from dataclasses import dataclass
from fastapi import Depends

@dataclass
class EmailRegisterParams:
  db: AsyncSession
  client_model: ClientAuthRegister

async def erm(
    db: Annotated[AsyncSession, Depends(get_db)],
    client_model: Annotated[ClientAuthRegister, Form()]
) -> EmailRegisterParams:
  return EmailRegisterParams(
    db=db,
    client_model=client_model
  )




