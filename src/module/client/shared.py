from typing import Optional, Annotated
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, ConfigDict, BeforeValidator
from src.shared.enums.constant import VerifyTokenType
from src.shared.schema.emptyString import empty_string
from src.shared.timestemp import get_timestamp

StringNotEmpty = Annotated[str, BeforeValidator(empty_string)]


class EmailBase(BaseModel):
  email: EmailStr = Field(...,examples=['anasothman@gmail.com'])
  is_verified: bool = False


class VerificationTokenBase(BaseModel):
  token: StringNotEmpty = Field(... , examples=['a1b2c3d4e5f6g7h8i9j0k'])
  token_type: VerifyTokenType
  expires_at: datetime = Field(..., examples=[get_timestamp()])

