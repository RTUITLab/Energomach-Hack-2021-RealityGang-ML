from pydantic import BaseModel
from typing import List, Dict


class Data(BaseModel):
    inn: str
    ogrn: str
    okved: List[str]
    osn_tass: str
    dop_tass: List[str]
    otr: List[str]
    attrs: List[str] = []
    region: str
    form: str


class Request(BaseModel):
    status: int
    data: Data


class Predictions(BaseModel):
    probs: Dict[str, float]
