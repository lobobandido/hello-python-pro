from typing import Optional

from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):  # type: ignore[call-arg,misc]
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
