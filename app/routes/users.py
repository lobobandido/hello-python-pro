from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.crud import create_user, delete_user, get_user, get_users
from app.db import get_session
from app.models import User

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=User)  # type: ignore[misc]
def api_create_user(user: User, session: Session = Depends(get_session)) -> User:
    return create_user(session, user)


@router.get("/", response_model=List[User])  # type: ignore[misc]
def api_list_users(session: Session = Depends(get_session)) -> List[User]:
    return get_users(session)


@router.get("/{user_id}", response_model=User)  # type: ignore[misc]
def api_get_user(user_id: int, session: Session = Depends(get_session)) -> User:
    user = get_user(session, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.delete("/{user_id}")  # type: ignore[misc]
def api_delete_user(
    user_id: int, session: Session = Depends(get_session)
) -> dict[str, bool]:
    delete_user(session, user_id)
    return {"ok": True}
