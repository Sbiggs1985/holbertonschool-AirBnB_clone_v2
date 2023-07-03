#!/usr/bin/python3
"""This module defines a class"""
"""from models.base_model import BaseModel"""

"""class User(BaseModel):"""
    """This class defines a user by various attributes"""
    """email = ''"""
    """password = ''"""
    """first_name = ''"""
    """last_name = ''"""

"""Above is the original code"""

from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.review import Review


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    places = relationship('Place', backref='user',
                          cascade='all, delete-orphan')
    reviews = relationship('Review', backref='user',
                           cascade='all, delete-orphan')
