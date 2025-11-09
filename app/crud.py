from sqlalchemy.exc import IntegrityError
from app.db import models
from app.db.session import SessionLocal
from app.core.security import get_password_hash
from sqlalchemy.orm import Session

def create_user(db: Session, email: str, password: str):
    user = models.User(email=email, hashed_password=get_password_hash(password))
    db.add(user)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise
    db.refresh(user)
    return user

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_note(db: Session, owner_id: int, title: str, content: str = "", public: bool = False):
    note = models.Note(owner_id=owner_id, title=title, content=content, public=public)
    db.add(note)
    db.commit()
    db.refresh(note)
    return note

def get_notes_for_user(db: Session, user_id: int):
    return db.query(models.Note).filter(models.Note.owner_id == user_id).all()
