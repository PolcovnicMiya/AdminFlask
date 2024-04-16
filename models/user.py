from sqlalchemy import Column, Integer, String, TIMESTAMP, func,ForeignKey, BigInteger,Date, Boolean
from sqlalchemy.orm import relationship

from database.database_connection import Base


class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=True, unique=True)
    hashed_password = Column(String(length=1024), nullable=True)
    registered_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

    role_id = Column(Integer)
    organization_id = Column(Integer, ForeignKey('Organization.id'))


