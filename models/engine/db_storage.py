#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


class DBStorage:
    """Represent database storage

    Attributes:
        __engine (sqlalchemy.Engine): SQlAlchemy database engine
        __session (sqlalchemy.Session): SQlAlchemy database session
    """
    __engine = None
    __session = None

    def __init__(self):
        """Create database engine with environment variables"""

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                getenv('HBNB_MYSQL_USER'),
                getenv('HBNB_MYSQL_PWD'),
                getenv('HBNB_MYSQL_HOST'),
                getenv('HBNB_MYSQL_DB'),
                pool_pre_ping=True))

        if getenv('HBNB_ENV') == 'test':
            # Drop all the tables
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session all objects depending of the class name

        if cls=None:
             query all types of objects (User, State, City, Amenity, Place and Review)

        Returns:
            a dictionary: key = <class-name>.<object-id>
        """
        dict = {}
        if cls and type(cls) == 'str':
            cls = eval(cls)
            query = self.__session.query(cls)
            for q in query:
                key = type(q).__name__ + '.' + q.id
                dict[key] = q
        else:
            classes = [User, State, City, Amenity, Place, Review]
            for cls in classes:
                query = self.__session.query(cls)
                for q in query:
                    key = type(q).__name__ + '.' + q.id
                    dict[key] = q
                # return {'{}.{}'.format(type(q).__name__, q.id): q for q in query}
        return dict

    def new(self, obj):
        """Add new object to the current database session (self.__session)"""
        self.__session.add(obj)
