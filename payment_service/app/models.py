from sqlalchemy import Column, Integer, String, Float, DateTime, Enum, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncAttrs

Base = declarative_base(cls=AsyncAttrs)

class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(50), nullable=False)
    amount = Column(Float, nullable=False)
    currency = Column(String(3), default="USD")
    status = Column(Enum("pending", "success", "failed", name="payment_status"), default="pending")
    transaction_id = Column(String(255), unique=True)
    callback_data = Column(String(1000))  # JSON string
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

# Unique index for transaction_id
from sqlalchemy import UniqueConstraint
UniqueConstraint(Payment.transaction_id)