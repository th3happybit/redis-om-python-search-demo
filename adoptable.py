from typing import Text
from redis_om import (Field, HashModel)
from redis_om import get_redis_connection

redis = get_redis_connection()

class Adoptable(HashModel):
    name: str = Field(index=True)
    species: str = Field(index=True)
    age: int = Field(index=True)
    weight: float = Field(index=True)
    sex: str = Field(index=True)
    fee: float = Field(index=True)
    children: str = Field(index=True)
    other_animals: str = Field(index=True)
    description: str = Field(index=True, full_text_search=True)

    class Meta:
        database = redis