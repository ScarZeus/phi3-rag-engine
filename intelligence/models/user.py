import uuid

from sqlalchemy import UUID, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID,
        primary_key=True,
        default=uuid.uuid4
    )

    username: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        unique=True
    )

    hash_password: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )