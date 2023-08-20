"""This module defines the States class
    that in turn defines the states table
    in the diclarative metadata
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """This class defines the table states"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                autoincrement='auto', nullable=False, unique=True)
    name = Column(String(128), nullable=False)
