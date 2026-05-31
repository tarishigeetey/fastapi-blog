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
    pass


class UserResponse(UserBase):
    model_config = ConfigDict(from_attributes=True)  # Allows parsing from ORM models
    id: int
    image_file: str | None
    image_path: str  # URL path to the user's profile image, included in responses


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


class PostBase(BaseModel):
    title: str = Field(
        min_length=1, max_length=100
    )  # Title of the post, required and limited to 100 characters
    content: str = Field(
        min_length=1
    )  # Content of the post, required and limited to 5000 characters


class PostCreate(PostBase):
    user_id: int  # TEMP


class PostResponse(PostBase):
    model_config = ConfigDict(from_attributes=True)  # Allows parsing from ORM models
    id: int  # Unique identifier for the post, included in responses
    user_id: int  # ID of the user who created the post, included in responses
    date_posted: datetime  # Date when the post was created, included in responses
    author: UserResponse  # Nested user information for the author of the post, included in responses


class PostUpdate(BaseModel):
    title: str | None = Field(
        default=None, min_length=1, max_length=100
    )  # Title of the post, required and limited to 100 characters
    content: str | None = Field(default=None, min_length=1)
