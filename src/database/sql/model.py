from .engine import Base
from sqlalchemy import String, Integer, Boolean, UUID, TIMESTAMP, ForeignKey, Enum as SqlEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
import uuid
from typing import Optional, List
from datetime import datetime


from src.shared.enums.constant import UserStatusEnum, VerifyTokenType, LanguageLocals, UserRole
from .mexin import TimestampMixin, IsVerifyMixin



class CountriesModel(TimestampMixin, Base):
  __tablename__ = 'countries'

  id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
  name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
  code: Mapped[str] = mapped_column(String(10), nullable=False, unique=True)

  Cities: Mapped[List["CitiesModel"]] = relationship(back_populates='countries', lazy="selectin")


class CitiesModel(TimestampMixin, Base):
  __tablename__ = 'cities'

  id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
  name: Mapped[str] = mapped_column(String, nullable=False, index=True, unique=True)
  country_id: Mapped[int] = mapped_column(ForeignKey('countries.id', ondelete='CASCADE'))

  Countries: Mapped["CountriesModel"] = relationship(back_populates='cities', lazy="selectin")
  Users: Mapped[List["UserModel"]] = relationship(back_populates='cities', lazy="selectin")


class UserModel(TimestampMixin, Base):
  __tablename__ = 'users'

  uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, index=True, default=uuid.uuid4)
  hash_password: Mapped[str] = mapped_column(String(128),nullable=False,)
  avatar_url: Mapped[Optional[str]] = mapped_column(String,default=None)

  status: Mapped[UserStatusEnum] = mapped_column(SqlEnum(UserStatusEnum, name='status_enum'), default=UserStatusEnum.ACTIVE)
  last_login_at: Mapped[Optional[datetime]] = mapped_column(TIMESTAMP(timezone=True), nullable=True)

  language: Mapped[LanguageLocals] = mapped_column(SqlEnum(LanguageLocals, name="language_enum"), default=LanguageLocals.EN)
  role: Mapped[UserRole] = mapped_column(SqlEnum(UserRole, name='user_role_enum'), default=UserRole.CLIENT)

  city_id: Mapped[Optional[int]] = mapped_column(ForeignKey('cities.id', ondelete='SET NULL'), default=None)
  Cities: Mapped[Optional["CitiesModel"]] = relationship(back_populates='users', lazy='selectin')

  Client: Mapped[Optional["ClientModel"]] = relationship(back_populates='users', lazy='selectin')
  Email: Mapped[Optional["EmailRegisterModel"]] = relationship(back_populates='users', lazy='selectin')
  Phone: Mapped[Optional["PhoneRegisterModel"]] = relationship(back_populates='users', lazy='selectin')
  Google: Mapped[Optional["GoogleRegisterModel"]] = relationship(back_populates='users', lazy='selectin')
  VerificationToken: Mapped["VerificationTokenModel"] = relationship(back_populates='users', lazy='selectin')


class EmailRegisterModel(TimestampMixin, IsVerifyMixin, Base):
  __tablename__ = 'email_register'

  id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
  email: Mapped[Optional[str]] = mapped_column(String(128), unique=True, default=None)

  user_uid: Mapped[Optional[uuid.UUID]] = mapped_column(ForeignKey('users.uid', ondelete='SET NULL'), unique=True)
  Users: Mapped["UserModel"] = relationship(back_populates='email', lazy='selectin')


class PhoneRegisterModel(TimestampMixin, IsVerifyMixin, Base):
  __tablename__ = 'phone_register'

  id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
  phone_number: Mapped[Optional[str]] = mapped_column(String, unique=True, default=None)

  user_uid: Mapped[Optional[uuid.UUID]] = mapped_column(ForeignKey('users.uid', ondelete='SET NULL'), unique=True)
  Users: Mapped["UserModel"] = relationship(back_populates='phone', lazy='selectin')


class GoogleRegisterModel(TimestampMixin, Base):
  __tablename__ = 'google_register'

  id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
  google_id: Mapped[Optional[str]] = mapped_column(String, unique=True, default=None)

  user_uid: Mapped[Optional[uuid.UUID]] = mapped_column(ForeignKey('users.uid', ondelete='SET NULL'), unique=True)
  Users: Mapped["UserModel"] = relationship(back_populates='google', lazy='selectin')


class ClientModel(TimestampMixin, Base):
  __tablename__ = 'client'

  uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, index=True, default=uuid.uuid4)
  name: Mapped[str] = mapped_column(String(256), nullable=False, index=True)
  user_uid: Mapped[uuid.UUID] = mapped_column(ForeignKey('users.uid', ondelete='SET NULL'), unique=True)

  Users: Mapped["UserModel"] = relationship(back_populates='client', lazy='selectin')



class VerificationTokenModel(TimestampMixin, Base):
  __tablename__ = 'verification_token'

  id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
  token: Mapped[str] = mapped_column(String, nullable=False, index=True)
  token_type: Mapped[VerifyTokenType] = mapped_column(SqlEnum(VerifyTokenType, name='verify_token_type'), nullable=False)
  used: Mapped[bool] = mapped_column(Boolean, default=False)
  expires_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True))

  user_uid: Mapped[Optional[uuid.UUID]] = mapped_column(ForeignKey('users.uid', ondelete='SET NULL'))
  Users: Mapped[Optional["UserModel"]] = relationship(back_populates='verification_token', lazy='selectin')



