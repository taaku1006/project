from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from db.base import Base
from sqlalchemy.orm import relationship

class Thread(Base):
    __tablename__ = "threads"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)

    messages = relationship("Message", back_populates="thread", cascade="all, delete")
