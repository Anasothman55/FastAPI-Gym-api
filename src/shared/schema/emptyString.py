from typing import AnyStr, Any
from pydantic import BaseModel
from pydantic_core.core_schema import ValidationInfo
from pydantic_core import PydanticCustomError


def empty_string(v: AnyStr, info: ValidationInfo):
  if v is None or (isinstance(v, str) and v.strip() == ""):
    raise PydanticCustomError(
      "empty_string",
      "String value must not be empty or only whitespace",
      {"field_name": info.field_name}
    )
  return v



class ErrorSchema(BaseModel):
  loc: tuple[str, ...] | list[str]
  type: str
  msg: str
  ctx: dict[str, Any] | None = None








