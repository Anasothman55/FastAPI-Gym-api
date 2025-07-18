from typing import Annotated
from sqlalchemy.ext.asyncio import  AsyncSession
from fastapi import  Form
from src.module.client.auth.schema.body import ClientAuthRegister, ClientAuthLogin
from src.shared.dependencies.db import get_db
from fastapi import Depends, Query

from . import EmailLoginParams
from .response_type import (
  EmailRegisterParams,
  EmailVerifyParams
)

async def erm(db: Annotated[AsyncSession, Depends(get_db)],body: Annotated[ClientAuthRegister, Form()]) -> EmailRegisterParams:
  """ Email Register Params Dependency """
  return EmailRegisterParams( db=db,body=body)


async def emp(token: Annotated[str, Query()], db: Annotated[AsyncSession, Depends(get_db)],)-> EmailVerifyParams:
  """ Email Verify Params Dependency """
  return EmailVerifyParams(db, token)


async def elp(db: Annotated[AsyncSession, Depends(get_db)], body: Annotated[ClientAuthLogin, Form()]) -> EmailLoginParams:
  """ Email Login Params Dependency """
  return EmailLoginParams( db=db, body= body)
