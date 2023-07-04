#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    __tablename__ = 'places'

    """ A place to stay """
    city_id = Column(String(60), nullible=False)
    user_id = Column(String(60), nullible=False)
    name = Column(String(128), nullible=False)
    description = Column(String(1024), nullible=False)
    number_rooms = Column(Integer, default=0, nullible=False)
    number_bathrooms = Column(Integer, default=0, nullible=False)
    max_guest = Column(Integer, default=0, nullible=False)
    price_by_night = Column(Integer, default=0, nullible=False)
    latitude = Column(Float, nullible=False)
    longitude = Column(Float, nullible=False)
    amenity_ids = []

    reviews = relationship("Review", cascade="all, delete", backref="place")
