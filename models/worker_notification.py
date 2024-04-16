from sqlalchemy import Column, String, DateTime, ForeignKey, BigInteger, Boolean
from sqlalchemy.orm import relationship
from database.database_connection import Base
from datetime import datetime


class WorkerNotification(Base):
    __tablename__ = "WorkerNotification"
    id = Column(BigInteger, primary_key=True)
    is_successful = Column(Boolean)
    text = Column(String)
    user_id = Column(BigInteger, ForeignKey('User.id'))
    organization_id = Column(BigInteger, ForeignKey('Organization.id'))
    resume_offer_id = Column(BigInteger, ForeignKey('ResumeOffer.id'))
    resume_offer = relationship("ResumeOffer", lazy="selectin")
    datetime = Column(DateTime, default=datetime.now)
    is_checked = Column(Boolean, default=False)
