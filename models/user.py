#!/usr/bin/python3
"""
    module containing user class
    module containing user class
"""
from models.base_model import BaseModel, Base
import models
from os import getenv
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, Column, Integer, String

storage_t = getenv("HBNB_TYPE_STORAGE")

class User(BaseModel, Base):
    """
        User class for the user
        User class for the user
    """
    if (storage_t == "db"):
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)

        places = relationship("Place", back_populates="user")
        reviews = relationship("Review", back_populates="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
