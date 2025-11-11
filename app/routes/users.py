from typing import List

from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.crud import create_user, delete_user, get_user, get_users, update_user
from app.db import get_session
from app.models import User

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=User)
def api_create_user(user: User, session: Session = Depends(get_session)):
    return create_user(session, user)


@router.get("/", response_model=List[User])
def api_list_users(session: Session = Depends(get_session)):
    return get_users(session)


@router.get("/{user_id}", response_model=User)
def api_get_user(user_id: int, session: Session = Depends(get_session)):
    return get_user(session, user_id)


@router.put("/{user_id}", response_model=User)
def api_update_user(user_id: int, user: User, session: Session = Depends(get_session)):
    return update_user(session, user_id, user)


@router.delete("/{user_id}")
def api_delete_user(user_id: int, session: Session = Depends(get_session)):
    delete_user(session, user_id)
    return {"message": "Usuario eliminado correctamente"}
