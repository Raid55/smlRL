""" Request model for sqlalchemy """

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Url(Base):
    '''
        defines url object to be stored in DB
    '''
    __tablename__ = "urls"
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True, unique=True)
    short_id = Column(String(8), nullable=False, unique=True)
    full_url = Column(String(2000), nullable=False)
    time_created = Column(DateTime, nullable=False, default=datetime.utcnow())
    time_created = Column(DateTime, nullable=True)

    def __str__(self):
        return  "[{}] | /{} == \"{}\" -- {} // {}".format(
            self.id,
            self.short_id,
            self.full_url,
            self.time_created,
            self.time_accessed
        )
