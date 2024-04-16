from sqlalchemy import Column, String, ForeignKey, BigInteger, Date, Boolean
from database.database_connection import Base



class Experience(Base):
    __tablename__ = "Experience"
    id = Column(BigInteger, primary_key=True)
    company_name = Column(String)
    description = Column(String)
    start_date = Column(Date)
    finish_date = Column(Date)
    is_work_now = Column(Boolean)
    resume_id = Column(BigInteger, ForeignKey("Resume.id"))