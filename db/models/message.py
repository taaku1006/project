from sqlalchemy import Column, Integer, String, Text, ForeignKey, CheckConstraint
from db.base import Base
from sqlalchemy.orm import relationship

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    thread_id = Column(Integer, ForeignKey("threads.id", ondelete="CASCADE"), nullable=False)
    sender_type = Column(String(20), nullable=False)
    content = Column(Text, nullable=False)

    __table_args__ = (
        CheckConstraint(
            "sender_type IN ('user', 'ai')", name="check_sender_type"
        ),
    )

    thread = relationship("Thread", back_populates="messages")
