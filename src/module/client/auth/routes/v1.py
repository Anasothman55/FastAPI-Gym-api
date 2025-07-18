
from typing import Annotated

from watchfiles import awatch

from src.module.client.auth.dependencies import (
  EmailRegisterParams,
  EmailVerifyParams,
  erm,
  emp,
  EmailLoginParams,
  elp
)
from fastapi import APIRouter, Depends, status

from ..schema.response import EmailVerifyResponse, EmailRegisterResponse, EmailLoginResponse
from ..service import email_register_service, verify_email_service, login_email_service

email = APIRouter(
  prefix='/email'
)


@email.post('/register', status_code=status.HTTP_201_CREATED, response_model=EmailRegisterResponse)
async def email_register(p: Annotated[EmailRegisterParams, Depends(erm)]): return await email_register_service(p.db, p.body)

@email.get('/verify', status_code=status.HTTP_200_OK, response_model=EmailVerifyResponse)
async def email_verify(p: Annotated[EmailVerifyParams, Depends(emp)]): return await verify_email_service(p.db,p.token)

@email.post('/login', response_model=EmailLoginResponse)
async def email_login(p: Annotated[EmailLoginParams, Depends(elp)]): return await login_email_service(p.db, p.body)

@email.post('/forgot-password')
async def email_forgot_password(): return 'email forgot password'

@email.post('/reset-password')
async def email_reset_password(): return 'email reset password'

@email.post('/logout')
async def email_logout(): return "email logout"

phone_number = APIRouter(
  prefix='/phone-number'
)


@phone_number.post('/register')
async def phone_number_register(): return "phone-number register"

@phone_number.post('/login')
async def phone_number_login(): return "phone-number login"

@phone_number.post('/verify')
async def phone_number_verify(): return 'phone-number verify'

@phone_number.post('/forgot-password')
async def phone_number_forgot_password(): return 'phone-number forgot password'

@phone_number.post('/reset-password')
async def phone_number_reset_password(): return 'phone-number reset password'

@phone_number.post('/logout')
async def phone_number_logout(): return "phone-number logout"


clientAuthRouter = APIRouter(
  tags=['Client-Auth'],
  prefix='/auth'
)

clientAuthRouter.include_router(email)
clientAuthRouter.include_router(phone_number)

@clientAuthRouter.post('/google', )
async def google_login(): return "google"

