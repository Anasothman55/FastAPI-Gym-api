from enum import StrEnum

class LoginProvider(StrEnum):
  EMAIL = 'email'
  PHONE_NUMBER = 'phone_number'
  GOOGLE = 'google'
  FACEBOOK = 'facebook'
  APPLE = 'apple'


class UserStatusEnum(StrEnum):
  ACTIVE = 'active'
  INACTIVE = 'inactive'
  SUSPEND = 'suspend'
  DELETE = 'delete'


class VerifyTokenType(StrEnum):
  EMAIL= 'email'
  PHONE_NUMBER = 'phone_number'


class TableStatus(StrEnum):
  ACTIVE = 'active'
  INACTIVE = 'inactive'
  DELETED = 'deleted'


class LanguageLocals(StrEnum):
  EN = 'en'
  AR = 'ar'
  KU = 'ku'



class UserRole(StrEnum):
  CLIENT = 'client'





