from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True)
    file_metadata = Column(JSONB)
