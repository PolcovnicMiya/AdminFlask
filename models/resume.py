from sqlalchemy import Column, String, ForeignKey, BigInteger, Date
from sqlalchemy.orm import relationship
from database.database_connection import Base


class Resume(Base):
    __tablename__ = "Resume"
    id = Column(BigInteger, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    gender = Column(String)
    region = Column(String)
    birthday = Column(Date)
    phone = Column(String)
    degree = Column(String)
    profession_id = Column(BigInteger, ForeignKey("Profession.id"))
    disability_id = Column(BigInteger, ForeignKey("DisabilityType.id"))
    user_id = Column(BigInteger, ForeignKey("User.id"))
    profession = relationship("Profession", lazy="selectin")
    disability_type = relationship("DisabilityType", lazy="selectin")

    experiences = relationship("Experience")

