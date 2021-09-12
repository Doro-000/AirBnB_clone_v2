#!/usr/bin/python3
"""
    module containing places to represent the place
    module containing places to represent the place
"""
from models.base_model import BaseModel, Base
from models.city import City
from models.user import User
from models.amenity import Amenity
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table

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
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey(City.id), nullable=False)
    user_id = Column(String(60), ForeignKey(User.id), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship("Review", backref="place")
    amenities = relationship("Amenity",
                             secondary=place_amenity, viewonly=False)

    @property
    def reviews(self):
        """getter function for reviews attribute"""
        result = []
        for review in self.reviews:
            if review.place_id == self.id:
                result.append(review)
        return result

    @property
    def amenities(self):
        """getter function for amenity attribute"""
        result = []
        for amenity in self.amenity_ids:
            if amenity == Amenity.id:
                result.append(amenity)
        return result

    @amenities.setter
    def amenities(self, obj):
        """ setter for amenities class """
        if (isinstance(obj, Amenity)):
            self.amenity_ids.append(obj.id)
