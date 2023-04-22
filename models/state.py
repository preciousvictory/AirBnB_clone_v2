#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
import models
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    
    if os.getenv('HBNB_TYPE_STORAGE') == "db":
        cities = relationship("City", backref="state", cascade="all, delete, delete-orphan")

    if os.getenv('HBNB_TYPE_STORAGE') != "db":
        @property
        def cities(self):
            """returns the list of City instances with state_id equals to the
            current State.id"""
            all_city = models.storage.all(City)
            list_city = []

            # copy values from dict to list
            for city in all_city.values():
                if city.state_id == self.id:
                    list_city.append(city)

            return list_city
