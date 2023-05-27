from fastapi import FastAPI

from house_on_treee.repository.db import MockDB
from house_on_treee.use_cases.use_cases import ChirpHandler
from house_on_treee.views.routes import api_router

# app = FastAPI(
#    title='REST API, FastApi+MongoDB',
#    description='This is simple REST API, realize CRUD operations with FastApi and MongoDB',
#    version='0.0.1.1.1',
#    # openapi_tags=tags_metadata,
# )
# app.include_router(api_router)


def create_app():
    app = FastAPI()
    db = MockDB()
    chirp_handler = ChirpHandler(db)
    return app, chirp_handler


# app, chirp_handler = create_app()

