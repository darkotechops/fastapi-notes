from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.schemas import NoteCreate, NoteRead
from app.db.session import get_db
from app.core.security import get_current_user
from app.crud import create_note, get_notes_for_user

router = APIRouter(prefix="/notes", tags=["notes"])

@router.post("/", response_model=NoteRead)
def create_note_route(note_in: NoteCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return create_note(db, owner_id=current_user.id, title=note_in.title, content=note_in.content, public=note_in.public)

@router.get("/", response_model=List[NoteRead])
def list_notes(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return get_notes_for_user(db, current_user.id)
