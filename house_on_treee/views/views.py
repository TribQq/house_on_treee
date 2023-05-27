from app import create_app  # , app, chirp_handler
from house_on_treee.domain.models import Chirp, User
from house_on_treee.serizalizers.models import ChirpPydanticModel

# from main import app, chirp_handler



app, chirp_handler = create_app()


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




