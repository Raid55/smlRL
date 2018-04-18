""" DB storage engine """

from os import getenv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlite3 import dbapi2 as sqlite
from models.url import Base


class DBStorage:
    """
        a connection for the database
    """
    __engine = None
    __session = None


    def __init__(self):
        """
            creating engine
        """
        self.__engine = create_engine(
            'sqlite+pysqlite:///smlUR.db', 
            native_datetime=True,
            module=sqlite, 
            pool_pre_ping=True, echo=False
        )

    def new(self, obj):
        """
            adding new obj to session queue
        """
        self.__session.add(obj)


    def query_by_id(self, object, key, id):
        return [str(o) for o in self.__session.query(object).filter(object[key] == id)][0]

    def save(self):
        """
            commiting session queue and database
        """
        self.__session.commit()

    def reload(self):
        """
            reload is in charge of creating table if
            it hasent been created and is also responsible
            for creating the session from the engine
            it is set to not expire on commit 
            so it stays connected through out 
            the apps life cylce
        """
        Base.metadata.create_all(self.__engine)
        sesh_maker = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        )
        self.__session = scoped_session(sesh_maker)

    def close(self):
        self.__session.remove()
