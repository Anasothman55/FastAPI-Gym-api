from sqlmodel import SQLModel, Field
from sqlalchemy import CheckConstraint, Column, TIMESTAMP
from pydantic import EmailStr
import uuid
from typing import Optional, List, Any
from datetime import date,datetime,time, timedelta,timezone
from src.shared.timestemp import get_timestamp, get_date, get_time




class UserEntity(SQLModel, table=True):
  __tablename__ = 'users'

  uid: uuid.UUID = Field(default_factory= uuid.uuid4, primary_key=True, index=True)
  name: str = Field(nullable=False, index=True, le=256)
  hash_password: str = Field(nullable=False)
  avatar_url: Optional[str]

  email: Optional[str] = Field(unique=True, index=True)
  email_verified: bool = Field(index=True, default=False)

  phone_number: Optional[str] = Field(unique=True, index=True)
  phone_number_verified: bool = Field(index=True, default=False)

  status: str = Field(max_length=50)

  last_login_at: Optional[datetime]
  created_at: datetime = Field(default_factory=get_timestamp,sa_column=Column(TIMESTAMP(timezone=True)))
  updated_at: datetime = Field(default_factory=get_timestamp,sa_column=Column(TIMESTAMP(timezone=True),onupdate=get_timestamp))
  delete_at: Optional[datetime]

  __table_args__ = (
    CheckConstraint("status IN ('anas', 'lat')", name="check_status_valid"),
  )










