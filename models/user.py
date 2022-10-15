#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column


class User(BaseModel, Base):
    """Representation of User class
    args:
        __tablename___(str): Name of the table
        name (String): name of users
        password (String): password of users
        first_name (String): first_name of users
        last_name (String): last_name of users
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
