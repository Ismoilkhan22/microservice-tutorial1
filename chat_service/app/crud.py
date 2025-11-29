from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from tenacity import retry, stop_after_attempt
from models import Message

@retry(stop=stop_after_attempt(3))
async def create_message(db: AsyncSession, sender_id: str, receiver_id: str, content: str) -> int:
    msg = Message(sender_id=sender_id, receiver_id=receiver_id, content=content)
    db.add(msg)
    await db.commit()
    await db.refresh(msg)
    return msg.id

async def get_messages(db: AsyncSession, user_id: str, limit: int = 50):
    stmt = select(Message).where(Message.sender_id == user_id).order_by(Message.timestamp.desc()).limit(limit)
    result = await db.execute(stmt)
    return result.scalars().all()