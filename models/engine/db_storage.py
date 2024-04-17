#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from sqlalchemy import create_engine
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
import os

class DBStorage():
    __engine = None
    __session = None
    hbnb_env = os.environ.get("HBNB_ENV")
    mysql_user = os.environ.get("HBNB_MYSQL_USER")
    mysql_pwd = os.environ.get("HBNB_MYSQL_PWD")
    mysql_host = os.environ.get("HBNB_MYSQL_HOST")
    mysql_db = os.environ.get("HBNB_MYSQL_DB")
    storage_type = os.environ.get("HBNB_TYPE_STORAGE")
    classes = ['User', 'Place', 'State', 'City',
               'Amenity', 'Review']
    def __init__(self):
        
        db_url= f"mysql+mysqldb://{
            self.mysql_user}:{self.mysql_pwd}@{self.mysql_host}/{self.mysql_db}"
        self.__engine = create_engine(db_url, pool_pre_ping=True)
        if self.hbnb_env == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """
        query on the current database session (self.__session)
        all objects depending of the class name (argument cls)
        """
        result = {}
        if cls:
            objects = self.__session.query(cls).all()
            for obj in objects:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                result[key] = obj
        else:
            for class_name in self.classes:
                objects = self.__session.query(class_name).all()
                for obj in objects:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    result[key] = obj
        return result

    def new(self, obj):
        """
        add the object to the current
        database session (self.__session)
        """
        self.__session.add(obj)

    def save(self):
        """
        commit all changes of the
        current database session (self.__session)
        """
        self.__session.commit()
    
    def delete(self, obj=None):
        """
        delete from the current database session obj if not None
        """
        if obj:
            self.__session.delete(obj)
    
    def reload(self):
        """
        create all tables in the database (feature of SQLAlchemy)
        (WARNING: all classes who inherit from Base must be imported before
        calling Base.metadata.create_all(engine)
        """
        from models.state import State
        from models.city import City
        Base.metadata.create_all(bind=self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
