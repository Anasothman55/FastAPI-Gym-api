from typing import Annotated
from sqlalchemy.ext.asyncio import  AsyncSession
from fastapi import  Form, Body
from src.module.client.auth.schema import ClientAuthRegister
from src.shared.dependencies.db import get_db
from dataclasses import dataclass
from fastapi import Depends

@dataclass
class EmailRegisterParams:
  db: AsyncSession
  body: ClientAuthRegister

async def erm(
    db: Annotated[AsyncSession, Depends(get_db)],
    body: Annotated[ClientAuthRegister, Form()]
) -> EmailRegisterParams:
  """ Email Register Params Dependency """
  return EmailRegisterParams(
    db=db,
    body=body
  )




