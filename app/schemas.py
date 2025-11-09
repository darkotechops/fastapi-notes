from pydantic import BaseModel, ConfigDict
from datetime import datetime

# 🧑‍💻 User Schemas
class UserCreate(BaseModel):
    email: str
    password: str


class UserRead(BaseModel):
    id: int
    email: str

    model_config = ConfigDict(from_attributes=True)


# 🧾 Token Schema (the one missing!)
class Token(BaseModel):
    access_token: str
    token_type: str


# 🗒️ Note Schemas
class NoteCreate(BaseModel):
    title: str
    content: str
    public: bool = False  


class NoteRead(BaseModel):
    id: int
    title: str
    content: str
    owner_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
