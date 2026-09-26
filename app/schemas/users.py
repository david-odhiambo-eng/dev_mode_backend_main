from pydantic import BaseModel, ConfigDict


class CreateUser(BaseModel):
    player_name: str
    email: str
    password: str


class CreateUserResponse(BaseModel):
    player_name: str
    model_config = ConfigDict(from_attributes=True)


class LoginUser(BaseModel):
    email: str
    password: str


class LoginUserResponse(BaseModel):
    player_name: str
    email: str
    access_token: str
    token_type: str
    model_config = ConfigDict(from_attributes=True)
