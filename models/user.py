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
from sqlalchemy import Column, String

class User(BaseModel, Base):
    """ User class """
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
