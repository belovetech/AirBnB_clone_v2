#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Create database engine with environment variables"""

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                getenv('HBNB_MYSQL_USER'),
                getenv('HBNB_MYSQL_PWD'),
                getenv('HBNB_MYSQL_DB'),
                pool_pre_ping=True))

        Session = sessionmaker()
        self.__session = Session()

        if getenv('HBNB_ENV') == 'test':
            # Drop all the tables
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """"""
