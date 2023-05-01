from datetime import datetime
from enum import Enum

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.dialects.postgresql import MONEY
from sqlalchemy.orm import relationship


# Base = declarative_base()

class Picture:
    ...

class Sex(Enum):
    male = 1
    female = 2


class User:
    """
    # доменная модель взаимодействия, удобна например для тестов т.к не нужно поднимать бд и тп.
    Дублирование репозиторной модели для бд.
    """

    def __init__(self, name: str,
                 avatar: Picture,
                 sex: str,
                 born_date: datetime,
                 pictures: list[Picture],
                 description: str,
                 ):
        self.name = name
        self.avatar = avatar
        self.sex = sex
        self.born_date = born_date
        self.pictures = pictures
        self.description = description

    # name = Column(String)


# class Chirp(Base):

class Chirp:
    """
    # доменная модель взаимодействия, удобна например для тестов т.к не нужно поднимать бд и тп.
    Дублирование репозиторной модели для бд.
    """
    def __init__(self,
                 author: User,
                 text: str,
                 publish_date: datetime,
                 is_draft: bool,
                 is_deleted: bool,
                 replies: list['Chirp'],
                 pictures: list[Picture],
                 # likes,
                 parent: 'Chirp' = None,
                 citate: 'Chirp' = None,

                 ):
        self.is_draft = is_draft
        self.is_deleted = is_deleted
        self.pictures = pictures
        self.author = author
        self.text = text
        self.replies = replies
        # self.likes = likes
        self.publish_date = publish_date
        self.parent = parent
        self.citate = citate
        
        # self.save()



    # author = relationship("Author", backref="chirps")
    # text = Column(String)
    # replies = ...
    # likes = ...
    # publish_date = Column(Date)



