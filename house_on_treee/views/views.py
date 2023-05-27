import uvicorn
from fastapi import FastAPI

from house_on_treee.domain.models import User, Chirp
from house_on_treee.repository.db import MockDB
from house_on_treee.serizalizers.models import ChirpPydanticModel
from house_on_treee.use_cases.use_cases import ChirpHandler

app = FastAPI()

db = MockDB()  # 4 test
chirp_handler = ChirpHandler(db) # 4 test


@app.post('/create')
async def create_chirp(chirp_data: ChirpPydanticModel):
    author_data = chirp_data.author
    author = User(name=author_data.name, born_date=author_data.born_date,
                  sex=author_data.sex, description=author_data.description)
    serialized_chirp = Chirp(author=author, publish_date=chirp_data.publish_date,
                             is_deleted=chirp_data.is_deleted, is_draft=chirp_data.is_draft,
                             text=chirp_data.text)
    chirp_handler.create_chirp(serialized_chirp)
    return {'response': 'chirp created successfully'}



if __name__ == '__main__':
    # r = get_chirps()
    # print(r)
    # uvicorn.run(api_router)
    uvicorn.run(app)

