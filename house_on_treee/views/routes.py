
from fastapi import APIRouter, FastAPI

from house_on_treee.repository.db import MockDB

api_router = APIRouter()

# @app.get('/chirps')


# @api_router.get('/chirps')
@api_router.get('/chirps')
def get_chirps():
    # db = MockDB()
    # chirps = db.read_chirp_from_db
    return {'HELLO': 'WORLD'}

#
# @app.get('/create')
# async def create_chirp(): # tmp test
#     return {'HELLO': 'WORLD, create chirp'}





