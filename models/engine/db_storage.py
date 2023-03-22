#!/usr/bin/python3
"""This module defines a class to manage New engine DB Storage AirBnB clone"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os


classes = {
    'BaseModel': BaseModel, 'User': User, 'Place': Place,
    'State': State, 'City': City, 'Amenity': Amenity,
    'Review': Review
}


class DBStorage:
    """This class manages DataBase storage of AirBnB clone project"""
    __engine = None
    __session = None

    def __init__(self):
        """method initialize the object's attributes """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.getenv('HBNB_MYSQL_USER'),
            os.getenv('HBNB_MYSQL_PWD'),
            os.getenv('HBNB_MYSQL_HOST'),
            os.getenv('HBNB_MYSQL_DB')), pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        dict_ = {}
        if cls is None:
            for clss in classes.values():
                result = self.__session.query(clss).all()

                for obj in result:
                    key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                    dict_[key] = obj
        else:
            clss = classes[cls]
            result = self.__session.query(clss).all()

            for obj in result:
                key = '{}.{}'.format(cls, obj.id)
                dict_[key] = obj

        return dict_

    def new(self, obj):
        """add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if not None:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """Loads storage from DB"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
