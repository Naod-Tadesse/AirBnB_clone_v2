#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, relationship

class Amenity(BaseModel, Base):
    """blue print for amenity"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)

