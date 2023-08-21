#!/usr/bin/python3
"""This module defines the Cities class
    and the cities table contents.
"""

from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import State, Base


class City(Base):
    """Defines Cities and cities
        by adding to the Declarative System metadata
        to enable creation of the table in
        a database that will be specified later
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
