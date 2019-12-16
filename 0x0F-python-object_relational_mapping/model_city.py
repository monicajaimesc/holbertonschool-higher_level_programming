#!/usr/bin/python3
"""
Definition for a state class
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State


class City(Base):
    """
    inherits from Base
    ID int in a column, is a primary key, autoincrements, can't be null
    Attribute Name string, can't be null
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id))
