from sqlalchemy import Column, String, BigInteger
from database.database_connection import Base



class Organization(Base):
    __tablename__ = "Organization"
    id = Column(BigInteger, primary_key=True)
    name = Column(String)
    description = Column(String)