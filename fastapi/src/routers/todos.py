from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from .. import models, schemas, auth
from ..dependencies import get_db

router = APIRouter()


@router.post("/", response_model=schemas.TodoCreate)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db),
                current_user: models.User = Depends(auth.get_current_user)):
    db_todo = models.Todo(**todo.dict(), owner_id=current_user.id)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


@router.get("/", response_model=List[schemas.TodoGet])
def read_todos(db: Session = Depends(get_db), current_user: models.User = Depends(auth.get_current_user), skip: int = 0,
               limit: int = 10):
    return db.query(models.Todo).filter(models.Todo.owner_id == current_user.id).offset(skip).limit(limit).all()


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, db: Session = Depends(get_db),
                current_user: models.User = Depends(auth.get_current_user)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id, models.Todo.owner_id == current_user.id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()
