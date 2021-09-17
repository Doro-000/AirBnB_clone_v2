#!/usr/bin/python3
"""
    module containing places to represent the place
    module containing places to represent the place
"""
from models.base_model import BaseModel, Base
import models
from os import getenv
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table


storage_t = getenv("HBNB_TYPE_STORAGE")

if (storage_t == "db"):
    place_amenity = Table('place_amenity', Base.metadata,
                        Column('place_id', String(60),
                                ForeignKey('places.id'),
                                primary_key=True, nullable=False),
                        Column('amenity_id', String(60),
                                ForeignKey('amenities.id'),
                                primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """
        Place class to represent places
        Place class to represent places
    """
    if (storage_t == "db"):
        __tablename__ = "places"

        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)

        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)

        amenity_ids = []
        amenities = relationship("Amenity",
                                secondary=place_amenity, viewonly=False, back_populates="place_amenities")

        user = relationship("User", back_populates="places")
        cities = relationship("City", back_populates="places")
        reviews = relationship("Review", back_populates="place")

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """getter function for reviews attribute"""
            result = []
            for review in models.storage.all(models.dummy_classes["Review"]).values():
                if review.place_id == self.id:
                    result.append(review)
            return result

        @property
        def amenities(self):
            """getter function for amenity attribute"""
            result = []
            for amenity in models.storage.all(models.dummy_classes["Amenity"]).values():
                if amenity.id in self.amenity_ids:
                    result.append()
            return result

        @amenities.setter
        def amenities(self, obj):
            """ setter for amenities class """
            if (isinstance(obj, models.dummy_classes["Amenity"])):
                self.amenity_ids.append(obj.id)
