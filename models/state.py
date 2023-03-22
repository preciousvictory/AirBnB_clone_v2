#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    if os.getenv('HBNB_TYPE_STORAGE') != "db":
        @property
        def cities(self):
            """returns the list of City instances with state_id equals to the
            current State.id"""
            all_city = storage.all(City)
            list_city = []
            for value in all_city.values():
                if city.state_id == self.id:
                    list_city.append(value)
            return list_city
