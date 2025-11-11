from typing import List, Optional

from fastapi import HTTPException, status
from sqlmodel import Session, select

from app.models import User


def create_user(session: Session, user: User) -> User:
    # Verificar si el email ya existe
    existing_user = session.exec(select(User).where(User.email == user.email)).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El correo ya está registrado.",
        )

    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def get_user(session: Session, user_id: int) -> Optional[User]:
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado."
        )
    return user


def get_users(session: Session) -> List[User]:
    return session.exec(select(User)).all()


def update_user(session: Session, user_id: int, updated_data: User) -> User:
    db_user = session.get(User, user_id)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado."
        )

    # Actualizar campos
    db_user.name = updated_data.name
    db_user.email = updated_data.email
    db_user.password = updated_data.password

    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


def delete_user(session: Session, user_id: int) -> None:
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado."
        )

    session.delete(user)
    session.commit()
