from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from typing import List

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)
    hashed_password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

    notes: List["Note"] = Relationship(back_populates="owner")

class Note(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    owner_id: int = Field(foreign_key="user.id", index=True)
    title: str
    body: str = ""
    public: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None

    owner: Optional[User] = Relationship(back_populates="notes")