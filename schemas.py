from datetime import (
    datetime,
)  # Importing datetime for handling date and time operations
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    EmailStr,
)  # BaseModel is used to create data models, ConfigDict is used for configuration, and Field is used to define field properties.


class UserBase(BaseModel):
    username: str = Field(
        min_length=1, max_length=50
    )  # Username of the user, required and limited to 50 characters
    email: EmailStr = Field(
        max_length=100
    )  # Email address of the user, validated as an email format


class UserCreate(UserBase):
    password: str = Field(
        min_length=8, max_length=255
    )  # Password for the user, required and limited to 255 characters


class UserPublic(UserBase):
    model_config = ConfigDict(from_attributes=True)  # Allows parsing from ORM models
    id: int
    username: str
    image_file: str | None
    image_path: str  # URL path to the user's profile image, included in responses


class UserPrivate(UserPublic):
    email: EmailStr  # Email address of the user, included in private responses


class UserUpdate(BaseModel):
    username: str | None = Field(
        default=None, min_length=2, max_length=50
    )  # Username of the user, required and limited to 50 characters
    email: EmailStr | None = Field(
        default=None, max_length=100
    )  # Email address of the user, validated as an email format
    image_file: str | None = Field(
        default=None
    )  # Optional field for the user's profile image file, included in update requests


class Token(BaseModel):
    access_token: (
        str  # The JWT access token string, included in authentication responses
    )
    token_type: str  # The type of the token (e.g., "bearer"), included in authentication responses


class PostBase(BaseModel):
    title: str = Field(
        min_length=1, max_length=100
    )  # Title of the post, required and limited to 100 characters
    content: str = Field(
        min_length=1
    )  # Content of the post, required and limited to 5000 characters


class PostCreate(PostBase):
    pass


class PostResponse(PostBase):
    model_config = ConfigDict(from_attributes=True)  # Allows parsing from ORM models
    id: int  # Unique identifier for the post, included in responses
    user_id: int  # ID of the user who created the post, included in responses
    date_posted: datetime  # Date when the post was created, included in responses
    author: UserPublic  # Nested user information for the author of the post, included in responses


class PostUpdate(BaseModel):
    title: str | None = Field(
        default=None, min_length=1, max_length=100
    )  # Title of the post, required and limited to 100 characters
    content: str | None = Field(default=None, min_length=1)
