
from typing import Annotated

from pydantic import BaseModel, ConfigDict, BeforeValidator, Field

from src.shared.schema.emptyString import empty_string

StringNotEmpty = Annotated[str, BeforeValidator(empty_string)]


class CitiesBase(BaseModel):
  name: StringNotEmpty = Field(examples=['Erbil'],min_length=2)

  model_config = ConfigDict(
    extra='forbid',
    str_strip_whitespace= True,
  )
