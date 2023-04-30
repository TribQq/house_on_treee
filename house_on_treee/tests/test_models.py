from datetime import datetime

import pytest
from house_on_treee.models import Chirp, User


def test_create_user():
    # user_valera = User.objects.create(name='Valera')
    # pytest.register_assert_rewrite()
    ...

def test_update_user():
    # chirp = Chirp.objects.get(pk=1, name='Valera')
    ...

def test_delete_user():
    # chirp = Chirp.objects.get(pk=1, name='Valera')
    ...


def test_create_chirp():
    # user_valera = User.objects.get(id=1)
    user_valera = User('Username_valera')
    datetime_now = datetime.now()
    # chirp = Chirp.objects.create(text='hello', author=user_valera, replies=[], likes=[], publish_date=datetime_now)
    chirp = Chirp(text='hello', author=user_valera, replies=[], likes=[], publish_date=datetime_now)
    # pytest.register_assert_rewrite()
    # assert chirp.user == user_valera
    assert chirp.text == 'hello'
    assert chirp.author == user_valera
    assert chirp.replies == []
    assert chirp.likes == []
    assert chirp.publish_date == datetime_now

def test_update_chirp():
    # chirp = Chirp.objects.get()
    ...

def test_delete_chirp():
    # chirp = Chirp.objects.get()
    ...

