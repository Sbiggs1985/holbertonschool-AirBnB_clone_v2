#!/usr/bin/python3
""" Imports the BaseModel and Base classes """
from models.base_model import BaseModel, Base
""" Imports the SQLalclchemy classes for defining columns """
from sqlalchemy import Column, String, ForeignKey

""" Defines a new class called 'Review' """
class Review(BaseModel, Base):
    __tablename__ = 'reviews'

""" Defines the column's named text, p;ace_id, and user_id """
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
