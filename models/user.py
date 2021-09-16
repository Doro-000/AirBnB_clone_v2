#!/usr/bin/python3
"""
    module containing user class
    module containing user class
"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, Column, Integer, String


class User(BaseModel, Base):
    """
        User class for the user
        User class for the user
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    places = relationship("Place", back_populates="user")
    reviews = relationship("Review", back_populates="user")
