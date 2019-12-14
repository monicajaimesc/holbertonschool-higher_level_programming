#!/usr/bin/python3
"""
Definition for a state class and an instance Base
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
# returns a new base class from which all mapped
# classes should inherit


class State(Base):
    """
    class attribute id that represents a column, unique integer, can't be null
    it's primary key
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
