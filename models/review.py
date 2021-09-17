#!/usr/bin/python3
"""
    contains review class to represent reviews
"""
from models.base_model import BaseModel, Base
import models
from os import getenv
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey

storage_t = getenv("HBNB_TYPE_STORAGE")


class Review(BaseModel, Base):
    """
        Review class
    """
    if (storage_t == "db"):
        __tablename__ = "reviews"
        place_id = Column(String(60), ForeignKey("places.id"))
        user_id = Column(String(60), ForeignKey("users.id"))
        text = Column(String(1024), nullable=False)

        user = relationship("User", back_populates="reviews")
        place = relationship("Place", back_populates="reviews")
    else:
        place_id = ""
        user_id = ""
        text = ""
