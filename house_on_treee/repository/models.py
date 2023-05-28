from contextlib import contextmanager
from typing import List

from sqlalchemy import Column, String, DateTime, Boolean, ForeignKey, Table, Date, Text, create_engine
from sqlalchemy.orm import declarative_base, mapped_column, Mapped, relationship, sessionmaker

# import sqlalchemy as sa

DeclarativeBaseModel = declarative_base()

engine = create_engine('sqlite:///house_on_tree_sqlite.db')  # создание связи с бд, с указанием относительного маршрута
SessionObj = sessionmaker(engine)


@contextmanager  # упрощенный аналог создания класса для with, без __enter__, __exit__, etc
def session_scope():
    """ открытие, закрытие, обработка исключений сессии"""
    session = SessionObj()
    try:
        yield session
    except Exception as e:
        session.rollback() # то , почему не использовали стандартный with
        raise e
    finally:
        session.close()


class PictureDb(DeclarativeBaseModel):
    __tablename__ = 'picture_table'

    uuid = Column(String, primary_key=True)
    user_uuid = Column(String, ForeignKey('user_table.uuid'), nullable=False)


class UserDb(DeclarativeBaseModel):
    __tablename__ = 'user_table'

    uuid = Column(String, primary_key=True)
    name = Column(String)
    # avatar =
    sex = Column(String)
    born_date = Column(Date)
    # pictures =
    description = Column(Text)


association_chirp_table = Table(
    "association_chirp_table",
    DeclarativeBaseModel.metadata,
    Column("chirp_uuid", ForeignKey("chirp_table.uuid")),
    Column("related_uuid", ForeignKey("chirp_table.uuid")),
)


class ChirpDb(DeclarativeBaseModel):
    __tablename__ = 'chirp_table'

    uuid = Column(String, primary_key=True)
    is_draft = Column(Boolean)
    is_deleted = Column(Boolean)
    # pictures =
    author_uuid = mapped_column(ForeignKey("user_table.uuid"))
    # author = mapped_column(ForeignKey("user_table.uuid"))
    text = Column(String)
    # replies: Mapped[List['ChirpDb']] = relationship(secondary=association_chirp_table) # many to many on yourself
    replies = relationship(
        'ChirpDb',
        secondary=association_chirp_table,
        primaryjoin=association_chirp_table.c.chirp_uuid == uuid,
        secondaryjoin=association_chirp_table.c.related_uuid == uuid,
        backref='chirps'
    )
    # likes =
    publish_date = Column(Date)
    parent_uuid = mapped_column(ForeignKey("chirp_table.uuid"))
    # citate =


class TestDb(DeclarativeBaseModel):
    __tablename__ = 'test_table'
    uuid = Column(String, primary_key=True)
    test_field = Column(String)


# async def create_table():
#     engine = database.url.dialect.create_connect_args(database.url)[0]
#     async with engine.connect() as conn:
#         await conn.run_sync(DeclarativeBaseModel.metadata.create_all)


# if __name__ == '__main__':
#     # db_session = session_scope()
#     with session_scope() as db_session:
#         # var = DeclarativeBaseModel.metadata.create_all
#
#         conn = engine.connect()
#         DeclarativeBaseModel.metadata.create_all(engine) # не пересоздается, если есть, если нет создаёт, но по хорошему прикрутить миграции(alembic какойнить)
#         # DeclarativeBaseModel.metadata.create_all(conn)
#         user = TestDb(test_field='User1', uuid='uuid_email1')
#         db_session.add(user)
#         db_session.commit()
#         db_session.refresh(user)
#         print({"user": user})
#         x = 5
