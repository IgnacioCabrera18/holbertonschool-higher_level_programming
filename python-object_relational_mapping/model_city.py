#!/usr/bin/python3
"""Module"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """Module"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    state_id = Column(Integer, ForeignKey('states.id'))
