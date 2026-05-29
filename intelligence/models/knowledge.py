from pgvector.sqlalchemy import Vector
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column
from sqlalchemy import Uuid
import uuid

class Base(DeclarativeBase):
    pass

class Knowledge(Base):
    __tablename__ = "knowledge_vector"

    document_name = mapped_column(String(30))
    chunk_id = mapped_column(
        Uuid, 
        primary_key=True, 
        default=uuid.uuid4
    )
    chunk_text = mapped_column(String())
