#!/usr/bin/python3
"""
    module containing Amenity class
"""
from models.base_model import BaseModel, Base
import models
from os import getenv
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Float, ForeignKey

storage_t = getenv("HBNB_TYPE_STORAGE")


class Amenity(BaseModel, Base):
    """
        Amenity class
    """

    if (storage_t == "db"):
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            "Place",
            secondary="place_amenity",
            back_populates="amenities")
    else:
        name = ""
