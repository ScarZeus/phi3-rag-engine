from pgvector.sqlalchemy import Vector
from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import String, Uuid
import uuid


class Base(DeclarativeBase):
    pass


class Knowledge(Base):
    __tablename__ = "knowledge_vector"

    chunk_id = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4
    )

    document_name = mapped_column(
        String(255),
        nullable=False
    )

    chunk_text = mapped_column(
        String,
        nullable=False
    )

    embedding = mapped_column(
        Vector(384),
        nullable=False
    )