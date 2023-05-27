import uvicorn

from house_on_treee.views.views import app

#
# from app import create_app
# app, chirp_handler = create_app()

if __name__ == '__main__':
    uvicorn.run(app=app)
