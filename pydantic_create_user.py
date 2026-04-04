from pydantic import BaseModel, Field, EmailStr, HttpUrl, ValidationError
import uuid


# {
#   "id": "string",
#   "email": "user@example.com",
#   "lastName": "string",
#   "firstName": "string",
#   "middleName": "string"
# }

class UserSchema(BaseModel):
    id: int
    email: EmailStr
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')



# {
#   "email": "user@example.com",
#   "password": "string",
#   "lastName": "string",
#   "firstName": "string",
#   "middleName": "string"
# }


class CreateUserRequestSchema(BaseModel):
    email: EmailStr
    password: str
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')

class CreateUserResponseSchema(BaseModel):
    """Описание структуры ответа создания пользователя."""
    user: UserSchema


