#!/usr/bin/python3
"""
    module containing Amenity class
"""
from models.base_model import BaseModel, Base
from models.city import City
from models.user import User
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Float, ForeignKey


class Amenity(BaseModel, Base):
    """
        Amenity class
    """

    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship(
        "Place",
        secondary="place_amenity",
        backref="amenities")
