from sqlalchemy.ext.asyncio import  AsyncSession
from src.module.client.auth.schema.body import ClientAuthRegister, ClientAuthLogin
from dataclasses import dataclass

@dataclass
class EmailRegisterParams:
  db: AsyncSession
  body: ClientAuthRegister

@dataclass
class EmailVerifyParams:
  db: AsyncSession
  token: str

@dataclass
class EmailLoginParams:
  db: AsyncSession
  body: ClientAuthLogin
