#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import models
import shlex


class State(BaseModel, Base):
    """Representation of State class
    args:
        __tablename___(str): Name of the table
        id (Integer): unique identifier of table's row
        name (String): name of states
        cities (Integer): State-City relationship
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City",
                          cascade='all, delete, delete-orphan', backref="states")

    @property
    def cities(self):
        """Get a list of all related City objects"""
        data = models.storage.all()
        lista = []
        result = []
        for key in data:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                lista.append(data[key])
        for elem in lista:
            if (elem.state_id == self.id):
                result.append(elem)
        return (result)