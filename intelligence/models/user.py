from sqlalchemy import UUID, String
from sqlalchemy.orm import DeclarativeBase, mapped_column
import uuid

class Base(DeclarativeBase):
    pass

class User(Base):

    __tablename__ = "users"


    user_id = mapped_column(
        UUID,
        primary_key= True,
        default=uuid.uuid4
    )
    username = mapped_column(String(30))
    hash_password = mapped_column(String(100))


    

    

    