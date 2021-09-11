#!/usr/bin/python3
"""
    contains state class to represent a state
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models

class State(BaseModel, Base):
    """ State class: class to represent states of cities"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

    @property
    def cities(self):
        result = []
        for city in models.storage.all(cls=models.dummy_classes["City"]).values():
            if city.state_id == self.id:
                result.append(city)
        return result
