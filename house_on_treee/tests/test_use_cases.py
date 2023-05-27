from datetime import datetime

from house_on_treee.domain.models import User, Chirp
from house_on_treee.repository.db import MockDB
from house_on_treee.use_cases.use_cases import ChirpHandler


def test_create_chirp():
    # mock example
    user_valera = User(name='Valera',
                       avatar=None,
                       sex='male',
                       born_date=datetime.now(),
                       pictures=None,
                       description='desc')
    chirp: Chirp = Chirp(author=user_valera, text='hello', publish_date=datetime.now(),
                         is_draft=False, is_deleted=False, replies=[], pictures=None,
                         parent=None, citate=None)
    db: MockDB = MockDB()
    db.save_chirps_to_db(chirps=[chirp])
    chirp_handler: ChirpHandler = ChirpHandler(db=db)
    chirp_handler.create_chirp(chirp=chirp)
    chirp_from_db = chirp_handler.read_chirp(uuid=chirp.uuid)
    assert chirp_from_db.uuid == chirp.uuid


def test_reply_chirp():
    # mock example
    user_valera = User(name='Valera',
                       avatar=None,
                       sex='male',
                       born_date=datetime.now(),
                       pictures=None,
                       description='desc')
    parent_chirp: Chirp = Chirp(author=user_valera, text='parent text', publish_date=datetime.now(),
                         is_draft=False, is_deleted=False, replies=[], pictures=None,
                         parent=None, citate=None)
    child_chirp: Chirp = Chirp(author=user_valera, text='child text', publish_date=datetime.now(),
                               is_draft=False, is_deleted=False, replies=[], pictures=None,
                               parent=None, citate=None)
    db: MockDB = MockDB()
    db.save_chirps_to_db(chirps=[parent_chirp])
    chirp_handler: ChirpHandler = ChirpHandler(db=db)
    chirp_handler.reply_chirp(child_chirp=child_chirp, parent_chirp=parent_chirp)
    chirp_handler.create_chirp(chirp=parent_chirp)

    parent_chirp_db: Chirp = chirp_handler.read_chirp(uuid=parent_chirp.uuid)
    child_chirp_from_db: Chirp = chirp_handler.read_chirp(uuid=child_chirp.uuid)

    assert parent_chirp_db.replies[0].uuid == child_chirp_from_db.uuid
    assert child_chirp_from_db.parent.uuid == parent_chirp_db.uuid
    assert child_chirp_from_db in parent_chirp_db.replies


    # chirp_from_db = read_chirp_from_db(chirp)


