from sqlalchemy import Column, String, BigInteger
from database.database_connection import Base


class Profession(Base):
    __tablename__ = "Profession"
    id = Column(BigInteger, primary_key=True)
    name = Column(String)

