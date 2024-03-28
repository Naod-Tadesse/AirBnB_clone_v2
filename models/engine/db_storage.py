#!/usr/bin/python3
"""
the database storage
"""
import sqlalchemy
import os
from models.base_model import Base
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity


class DBStorage:
    """
    storage class for database
    """
    __session = None
    __engine = None
    class_list = {
            'User': User, 'Place': Place, 'State': State,
            'City': City, 'Amenity': Amenity, 'Review': Review
           }

    def __init__(self):
        USER = os.getenv('HBNB_MYSQL_USER')
        PASS = os.getenv('HBNB_MYSQL_PWD')
        HOST = os.getenv('HBNB_MYSQL_HOST')
        DB = os.getenv('HBNB_MYSQL_DB')
        ENV = os.getenv('HBNB_ENV')
        self.__engine = sqlalchemy.create_engine(
            f'mysql+mysqldb://{USER}:{PASS}@{HOST}/{DB}',
            pool_pre_ping=True)
        if ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, name=None):
        """this method querys database"""
        res = {}
        for k, v in DBStorage.class_list.items():
            if not name:
                qr = self.__session.query(DBStorage.class_list[k])
                for i in qr:
                    res[i.__class__.__name__ + '.' + i.id] = i
            elif name == k:
                qr = self.__session.query(DBStorage.class_list[k]).all()
                for i in qr:
                    res[i.__class__.__name__ + '.' + i.id] = i
            else:
                pass
        return res

    def new(self, obj):
        """entry new"""
        self.__session.add(obj)

    def close(self):
        """the session closing"""
        self.__session.close()

    def save(self):
        """persist change"""
        self.__session.commit()

    def delete(self, obj=None):
        """"this handles deleting"""
        if not obj:
            pass
        else:
            self.__session.delete(obj)

    def reload(self):
        """handler for connection"""
        connection = sqlalchemy.orm.sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Base.metadata.create_all(self.__engine)
        self.__session = sqlalchemy.orm.scoped_session(connection)()
