from typing import Annotated
from pydantic import BaseModel, ConfigDict, BeforeValidator, Field
from src.database.sql.model import UserModel, ClientModel, EmailRegisterModel
from src.shared.schema.emptyString import empty_string

StringNotEmpty = Annotated[str, BeforeValidator(empty_string)]


class ClientBase(BaseModel):
  name: StringNotEmpty = Field(examples=['Anas Othman'],min_length=2)

  model_config = ConfigDict(
    extra='forbid',
    str_strip_whitespace= True,
  )



class ClientCreateTypeResponse(BaseModel):
  user: UserModel
  client: ClientModel
  email: EmailRegisterModel

  model_config = ConfigDict(arbitrary_types_allowed=True)
