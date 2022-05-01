from typing import List
from typing import Optional

from pydantic import (
    BaseModel, 
    Field, 
    validator
)

class Customer(BaseModel):
    first_name: str = Field(..., example="Akintunde", alias="first-name")
    middle_name: str = Field(default="", example="Oluwatobiloba", alias="middle-name")
    surname: str = Field(..., example="Oladipo", alias="last-name")

    @validator('*', pre=True)
    def to_lower(cls, name: str):
        return name.lower().strip()

    class Config:
        allow_population_by_field_name = True


class CustomerList(BaseModel):
    customers: List[Customer]

    class Config:
        schema_extra = {
            "example": {
                "customers": [
                    {
                        "first_name": "Jummy",
                        "middle_name": "",
                        "surname": "Plc."
                    }
                ]
            }
        }


# TODO: Include defaults for candidate and match score?
class Vote(BaseModel):
    vote: bool = Field(..., example=False)
    candidate: Optional[str] = Field(example="Akintunde Oladipo")
    match_score: float = Field(example=84)
