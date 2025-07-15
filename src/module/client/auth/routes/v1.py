from ..dependencie import erm, EmailRegisterParams

from typing import Annotated,Any

from fastapi import APIRouter, Depends

from ..schema import ClientAuthRegisterResponseEmail

email = APIRouter(
  prefix='/email'
)

@email.post('/register', response_model=ClientAuthRegisterResponseEmail)
async def email_register(p: Annotated[EmailRegisterParams, Depends(erm)]): return p.client_model

@email.post('/login')
async def email_login(): return "email login"

@email.post('/verify')
async def email_verify(): return 'email verify'

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

