from datetime import datetime

from house_on_treee.domain.models import User, Chirp
from house_on_treee.use_cases.use_cases import save_chirp_to_db


def test_save_chirp_to_db():
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
    save_chirp_to_db(chirp=chirp)
    # chirp_from_db = read_chirp_from_db(chirp)


