import uuid
import datetime

from pydantic import dataclasses, BaseModel
from pydantic.dataclasses import dataclass

from house_on_treee.domain.models import Picture


# @dataclass
# class UserPydanticModel(BaseModel):
@dataclass
class UserPydanticModel:
    # uuid: uuid.UUID
    name: str
    born_date: datetime.datetime
    description: str
    # avatar: Picture
    sex: str
    # pictures: list[Picture]
    description: str


# @dataclass
# class ChirpPydanticModel(BaseModel):
@dataclass
class ChirpPydanticModel:
    uuid: uuid.UUID
    author: UserPydanticModel
    text: str
    publish_date: datetime.datetime
    is_draft: bool
    is_deleted: bool
    # replies: list['ChirpPydanticModel']
    # pictures: list[Picture]
    # parent: 'ChirpPydanticModel'
    # citate: 'ChirpPydanticModel'


