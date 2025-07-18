from typing import Annotated, Optional
from pydantic import BaseModel, BeforeValidator, Field, EmailStr, ConfigDict
from src.shared.enums.constant import LanguageLocals
from src.shared.schema.emptyString import empty_string

StringNotEmpty = Annotated[str, BeforeValidator(empty_string)]


class ClientAuthBase(BaseModel):
  email: EmailStr = Field(..., examples=['anasothman@gmail.com'], exclude=True)
  password: StringNotEmpty = Field(..., examples=['fastapi1234'] , min_length=8)

  model_config = ConfigDict(
    extra='forbid',
    str_strip_whitespace= True,
  )

class ClientAuthRegister(ClientAuthBase):
  name: StringNotEmpty = Field(examples=['Anas Othman'],min_length=2)
  language: Optional[LanguageLocals] = Field(default= LanguageLocals.EN ,description="""This data come from local storage or browser language user can't have this field""")


class ClientAuthLogin(ClientAuthBase):
  pass









