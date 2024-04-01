#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship(
            "City", backref="state", cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            """get cities"""
            from models import storage
            result = [
                city for city in storage.all("City").values()
                if city.state_id == self.id
            ]
            return result
