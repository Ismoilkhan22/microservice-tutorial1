from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncAttrs

Base = declarative_base(cls=AsyncAttrs)

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(String(50), ForeignKey("users.id"), nullable=False)  # Users table qo'shsa bo'ladi
    receiver_id = Column(String(50), nullable=False)
    content = Column(String(500), nullable=False)
    is_read = Column(False, default=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

# Index on sender_id + timestamp for pagination
from sqlalchemy import Index
Index('idx_messages_sender_time', Message.sender_id, Message.timestamp)