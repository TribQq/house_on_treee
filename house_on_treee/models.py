from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.dialects.postgresql import MONEY
from sqlalchemy.orm import relationship


# Base = declarative_base()


# class User(Base):
# name = Column(String)
class User:
    def __init__(self, name):
        self.name = name
    # name = Column(String)


# class Chirp(Base):
class Chirp:
    def __init__(self, author: User, text: str, replies, likes, publish_date: datetime):
        self.author = author
        self.text = text
        self.replies = replies
        self.likes = likes
        self.publish_date = publish_date
        # self.save()



    # author = relationship("Author", backref="chirps")
    # text = Column(String)
    # replies = ...
    # likes = ...
    # publish_date = Column(Date)



