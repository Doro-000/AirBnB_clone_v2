#!/usr/bin/python3
"""
    contains state class to represent a state
"""

from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

storage_t = getenv("HBNB_TYPE_STORAGE")

class State(BaseModel, Base):
    """ State class: class to represent states of cities"""
    if (storage_t == "db"):
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

        @property
        def cities(self):
            result = []
            pep_fix = models.dummy_classes["City"]
            for city in models.storage.all(cls=pep_fix).values():
                if city.state_id == self.id:
                    result.append(city)
            return result
