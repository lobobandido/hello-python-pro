from typing import List, Optional, cast

from sqlmodel import Session, select

from app.models import User


def create_user(session: Session, user: User) -> User:
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def get_users(session: Session) -> List[User]:
    """Devuelve la lista de usuarios."""
    users = session.exec(select(User)).all()
    return cast(List[User], users)


def get_user(session: Session, user_id: int) -> Optional[User]:
    """Obtiene un usuario por ID."""
    user = session.get(User, user_id)
    return cast(Optional[User], user)


def delete_user(session: Session, user_id: int) -> None:
    user = session.get(User, user_id)
    if user:
        session.delete(user)
        session.commit()
