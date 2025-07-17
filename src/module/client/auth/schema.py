from typing import Annotated, Optional, List

from pydantic import BaseModel, BeforeValidator, Field, EmailStr, ConfigDict

from src.module.client.shared import EmailBase, VerificationTokenBase
from src.module.common.cities.schema import CitiesBase
from src.shared.enums.constant import LanguageLocals, StatusEnum, UserRole
from src.shared.schema.emptyString import empty_string
from src.module.client.client.schema import ClientBase

StringNotEmpty = Annotated[str, BeforeValidator(empty_string)]


class ClientAuthBase(BaseModel):
  email: EmailStr = Field(..., examples=['anasothman@gmail.com'])
  password: StringNotEmpty = Field(..., examples=['fastapi1234'] , min_length=8)

  model_config = ConfigDict(
    extra='forbid',
    str_strip_whitespace= True,
  )

class ClientAuthRegister(ClientAuthBase):
  name: StringNotEmpty = Field(examples=['Anas Othman'],min_length=2)
  language: Optional[LanguageLocals] = Field(default= LanguageLocals.EN ,description="""This data come from local storage or browser language user can't have this field""")




class ClientAuthRegisterResponseBase(BaseModel):
  language: LanguageLocals
  status: StatusEnum
  role: UserRole
  avatar_url: Optional[str]
  Client: ClientBase
  Cities: Optional[CitiesBase] = {}

class ClientAuthRegisterResponseEmail(ClientAuthRegisterResponseBase):
  Email: EmailBase



class ClientAuthLogin(ClientAuthBase):
  pass







