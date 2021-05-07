from typing import List

from pydantic import BaseModel, Field


class LookupRequest(BaseModel):
    word: str = Field(..., description="Input word", min_length=1)


class LookupResponse(BaseModel):
    input_word: str = Field(..., description="Original word from input", alias='inputWord')
    most_frequent: str = Field(None, description="Most frequent word", alias='mostFrequent')
    closest_words: List[str] = Field(None, description="Most closest words by edit distance", alias="closestWords")

    class Config:
        allow_population_by_field_name = True
