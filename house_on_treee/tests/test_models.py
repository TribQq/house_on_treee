from datetime import datetime

# import pytest
from house_on_treee.domain.models import Chirp, User


def test_create_user():

    datetime_now = datetime.now()
    user_valera = User(name='Valera',
                       avatar=None,
                       sex='male',
                       born_date=datetime_now,
                       pictures=None,
                       description='desc')
    assert user_valera.name == 'Valera'
    assert user_valera.avatar == None
    assert user_valera.born_date == datetime_now
    assert user_valera.pictures == None
    assert user_valera.description == 'desc'

def test_update_user():
    # chirp = Chirp.objects.get(pk=1, name='Valera')
    ...

def test_delete_user():
    # chirp = Chirp.objects.get(pk=1, name='Valera')
    ...


def test_create_chirp():
    # user_valera = User.objects.get(id=1)
    user_valera = User(name='Valera',
                       avatar=None,
                       sex='male',
                       born_date=datetime.now(),
                       pictures=None,
                       description='desc')
    datetime_now = datetime.now()
    # chirp = Chirp.objects.create(text='hello', author=user_valera, replies=[], likes=[], publish_date=datetime_now)
    # chirp = Chirp(text='hello', author=user_valera, replies=[], likes=[], publish_date=datetime_now)
    chirp = Chirp(author=user_valera,text='hello',   publish_date=datetime_now,
                  is_draft=False, is_deleted=False, replies=[], pictures=None,
                  parent=None, citate=None)
    # pytest.register_assert_rewrite()
    # assert chirp.user == user_valera
    assert chirp.text == 'hello'
    assert chirp.author == user_valera
    assert chirp.replies == []
    # assert chirp.likes == []
    assert chirp.publish_date == datetime_now


def test_update_chirp():
    # chirp = Chirp.objects.get()
    ...

def test_delete_chirp():
    # chirp = Chirp.objects.get()
    ...

