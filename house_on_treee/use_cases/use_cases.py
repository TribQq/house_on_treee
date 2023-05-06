from datetime import datetime

from house_on_treee.domain.models import User, Picture, Chirp
from house_on_treee.repository.db import AbstractDataBase


class ChirpHandler:

    def __init__(self, db: AbstractDataBase):
        self.db = db

    def create_chirp(self, chirp: Chirp):
        self.db.save_chirps_to_db(chirps=[chirp])

    def read_chirp(self, uuid: str):
        return self.db.read_chirp_from_db(uuid=uuid)

    def reply_chirp(self, child_chirp: Chirp, parent_chirp: Chirp):
        parent_chirp.replies.append(child_chirp)
        child_chirp.parent = parent_chirp
        self.db.save_chirps_to_db(chirps=[child_chirp, parent_chirp])



