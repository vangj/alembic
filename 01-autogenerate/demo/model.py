from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    password = Column(String, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
