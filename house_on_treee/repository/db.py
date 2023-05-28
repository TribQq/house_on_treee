# доступ к базе
from abc import ABC

from house_on_treee.domain.models import Chirp


class AbstractDataBase(ABC):

    def read_chirp_from_db(self, uuid):
        raise NotImplementedError

    def save_chirps_to_db(self, chirps: list[Chirp]):
        raise NotImplementedError


class MockDB(AbstractDataBase):  # класс заглушка, пока нет бд
    def __init__(self):
        self.chirps = {}

    def read_chirp_from_db(self, uuid):
        return self.chirps[uuid]

    def save_chirps_to_db(self, chirps: list[Chirp]):
        for chirp in chirps:
            self.chirps[chirp.uuid] = chirp


class SqLiteDB(AbstractDataBase):  # класс заглушка, пока нет бд
    def __init__(self):
        ...

    def read_chirp_from_db(self, uuid):
        ...

    def save_chirps_to_db(self, chirps: list[Chirp]):
        ...

