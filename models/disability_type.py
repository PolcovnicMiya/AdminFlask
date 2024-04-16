from sqlalchemy import Column, String, BigInteger
from database.database_connection import Base



class DisabilityType(Base):
    __tablename__ = "DisabilityType"
    id = Column(BigInteger, primary_key=True)
    name = Column(String, nullable=False, unique=True)
