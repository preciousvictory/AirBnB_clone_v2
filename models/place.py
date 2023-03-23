#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from models.review import Review
import os


if os.getenv('HBNB_TYPE_STORAGE') == "db":
    place_amenity = Table('place_amenity', Base.metadata,
                        Column('place_id', String(60),
                               ForeignKey('places.id'), primary_key=True,
                               nullable=False),
                        Column('amenity_id', String(60), 
                               ForeignKey('amenities.id'), primary_key=True,
                               nullable=False)
    )


class Place(BaseModel, Base):
    """ A place to stay """
    if os.getenv('HBNB_TYPE_STORAGE') == "db":
        __tablename__ = 'places'
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
        reviews = relationship("Review", backref="place", cascade="all, delete")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 backref="place" , viewonly=False)
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
            """ returns the list of Review instances with place_id equals to
            the current Place.id"""
            all_reviews = storage.all(Review)
            list_rev = []
            for value in all_reviews.values():
                if review.place_id == Place.id:
                    list_rev.append(value)
            return list_rev
        @property
        def amenities(self):
            """returns the list of Amenity instances based on the attribute
            amenity_ids that contains all Amenity.id linked to the Place"""
            all_ameniies = storage.all(Amenity)
            list_ame = []
            for value in all_amenities.values():
                if value.id in self.amenity_ids:
                    list_ame.append(value)
            return list_ame

        @amenities.setter
        def amenities(self, obj):
            """Setter attribute amenities that handles append method foradding
            an Amenity.id to the attribute amenity_ids. """
            from models.amenity import Amenity
            if isinstance(obj, Amenity) and type(obj) == Amenity:
                self.amenity_ids.append(obj.id)
