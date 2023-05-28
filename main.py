import uvicorn

from house_on_treee.repository.models import session_scope, DeclarativeBaseModel, engine, TestDb
from house_on_treee.views.views import app

#
# from app import create_app
# app, chirp_handler = create_app()


def create_non_exists_db_table():
    DeclarativeBaseModel.metadata.create_all(engine)
    # создает только посе стопа
    with session_scope() as db_session:
        conn = engine.connect()
        try:
            test_db_user = TestDb(test_field='User0', uuid='uuid_email0')  # данные внёс.

            db_session.add(test_db_user)
            db_session.commit()
            db_session.refresh(test_db_user)
            print({"test_db_user": test_db_user})
        except Exception as e:
            print(f'Error:\n {e}')
        
        
if __name__ == '__main__':
    create_non_exists_db_table()
    uvicorn.run(app=app)
