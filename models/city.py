#!/usr/bin/python3
"""
    contains City class to represent a city
    contains City class to represent a city
"""

from models.base_model import BaseModel, Base
from models.state import State
from os import getenv
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey

storage_t = getenv("HBNB_TYPE_STORAGE")


class City(BaseModel, Base):
    """ City class :City class to represent a city
    City class :City class to represent a city"""

    if (storage_t == "db"):
        __tablename__ = "cities"
        state_id = Column(String(60), ForeignKey(State.id))
        name = Column(String(128), nullable=False)
        places = relationship("Place", back_populates="cities")
        state = relationship("State", back_populates="cities")
    else:
        state_id = ""
        name = ""
