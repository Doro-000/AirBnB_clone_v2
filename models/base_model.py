#!/usr/bin/python3
"""
    Module containing BaseModel
"""
from uuid import uuid4
from datetime import datetime
import models
from os import getenv
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

storage_t = getenv("HBNB_TYPE_STORAGE")
if (storage_t == "db"):
    Base = declarative_base()
else:
    Base = object


class BaseModel():
    """
        Base class to define all common attributes and methods for
        other classes
    """
    if (storage_t == "db"):
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
        updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """
            initialization of BaseModel
        """
        if kwargs:
            for key in kwargs:
                if key == "__class__":
                    continue
                elif key in ("created_at", "updated_at"):
                    iso = "%Y-%m-%dT%H:%M:%S.%f"
                    setattr(self, key, datetime.strptime(kwargs[key], iso))
                else:
                    setattr(self, key, kwargs[key])
                self.id = str(uuid4())
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """
            return string representation of a Model
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
            update latest updation time of a model
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
            custom representation of a model
        """
        copy_dict = self.__dict__.copy()
        custom_dict = {}
        custom_dict.update({"__class__": self.__class__.__name__})
        for key in list(copy_dict):
            if key in ("created_at", "updated_at"):
                custom_dict.update({key: getattr(self, key).isoformat()})
            elif key == "_sa_instance_state":
                copy_dict.pop(key)
            else:
                custom_dict.update({key: getattr(self, key)})
        return custom_dict

    def delete(self):
        """ delete the current instance from the storage
        """
        models.storage.delete(self)
