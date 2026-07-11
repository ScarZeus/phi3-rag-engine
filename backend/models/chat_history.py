from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import UUID, ForeignKey, String
import uuid

class Base(DeclarativeBase):
    pass

class ChatHistory(Base):

    __tablename__= "chat_history"
    chat_id = mapped_column(
        UUID,
        primary_key=True,
        default=uuid.uuid4
    )
    chat_history_title = mapped_column(
        String(150)
    )
    user_id = mapped_column(ForeignKey("users.user_id"))
    