from typing import Annotated, Optional, Any
from pydantic import BaseModel, BeforeValidator, Field, EmailStr, ConfigDict

from src.module.client.client.schema import ClientBase
from src.module.client.shared import EmailBase
from src.module.common.cities.schema import CitiesBase
from src.shared.enums.constant import StatusEnum, UserRole
from src.shared.schema.emptyString import empty_string
from datetime import datetime



StringNotEmpty = Annotated[str, BeforeValidator(empty_string)]




class EmailRegisterResponse(BaseModel):
  msg: str = Field(...)


class EmailVerifyResponse(EmailBase):
  pass

  model_config = ConfigDict(from_attributes=True)





class EmailBase(BaseModel):
  email: str
  is_verified: bool
  verified_at: datetime | None = None

class PhoneBase(BaseModel):
  phone_number: str
  is_verified: bool
  verified_at: datetime | None = None

class GoogleBase(BaseModel):
  google_id: str


class EmailLoginResponse(BaseModel):
  status: StatusEnum
  avatar_url: str | None = None
  role: UserRole
  Email: EmailBase | None = None
  Client: ClientBase
  Cities: CitiesBase | None = None
  Phone: PhoneBase | None = None
  Google: GoogleBase | None = None











