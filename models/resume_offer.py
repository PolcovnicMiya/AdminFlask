import datetime as datetime
from sqlalchemy import Column, ForeignKey, BigInteger, DateTime
from sqlalchemy.orm import relationship
from database.database_connection import Base
from datetime import datetime


class ResumeOffer(Base):
    __tablename__ = "ResumeOffer"
    id = Column(BigInteger, primary_key=True)
    resume_id = Column(BigInteger, ForeignKey("Resume.id"))
    offer_id = Column(BigInteger, ForeignKey("Offer.id"))
    datetime = Column(DateTime, default=datetime.now)
    resume = relationship("Resume", lazy="selectin")
