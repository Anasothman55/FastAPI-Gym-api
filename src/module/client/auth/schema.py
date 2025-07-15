from typing import Annotated, Optional

from pydantic import BaseModel, BeforeValidator, Field, EmailStr, ConfigDict

from src.module.client.shared import EmailBase, VerificationTokenBase
from src.module.common.cities.schema import CitiesBase
from src.shared.enums.constant import LanguageLocals, UserStatusEnum, UserRole
from src.shared.schema.emptyString import empty_string
from src.module.client.client.schema import ClientBase

StringNotEmpty = Annotated[str, BeforeValidator(empty_string)]


class ClientAuthBase(BaseModel):
  password: StringNotEmpty = Field(..., examples=['fastapi1234'] , min_length=8, exclude=True)
  email: EmailStr = Field(..., examples=['anasothman@gmail.com'])

  model_config = ConfigDict(
    extra='forbid',
    str_strip_whitespace= True,
  )

class ClientAuthRegister(ClientAuthBase):
  name: StringNotEmpty = Field(examples=['Anas Othman'],min_length=2)
  language: Optional[LanguageLocals] = Field( default= LanguageLocals.EN)


class ClientAuthRegisterResponseBase(BaseModel):
  language: LanguageLocals
  status: UserStatusEnum
  role: UserRole
  avatar_url: Optional[str]
  Client: ClientBase
  Cities: CitiesBase
  VerificationToken: VerificationTokenBase

class ClientAuthRegisterResponseEmail(ClientAuthRegisterResponseBase):
  Email: EmailBase



class ClientAuthLogin(ClientAuthBase):
  pass








