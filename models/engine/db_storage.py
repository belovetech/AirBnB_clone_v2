#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Create database engine with environment variables"""
        load_dotenv()
        user = os.environ['HBNB_MYSQL_USER']
        passwd = os.environ['HBNB_MYSQL_PWD']
        db = os.environ['HBNB_MYSQL_DB']
        host = os.environ['HBNB_MYSQL_HOST']
        env = os.environ['HBNB_ENV']

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(user, passwd, host, db, pool_pre_ping=True))

        Session = sessionmaker()
        self.__session = Session()

        if env == 'test':
            # Drop all the tables
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """"""
