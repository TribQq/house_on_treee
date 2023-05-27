from fastapi import FastAPI

from house_on_treee.views.routes import api_router

app = FastAPI(
   title='REST API, FastApi+MongoDB',
   description='This is simple REST API, realize CRUD operations with FastApi and MongoDB',
   version='0.0.1.1.1',
   # openapi_tags=tags_metadata,
)

app.include_router(api_router)
