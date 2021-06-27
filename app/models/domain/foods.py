from typing import List

from app.models.common import DateTimeModelMixin, IDModelMixin
from app.models.domain.profiles import Profile
from app.models.domain.rwmodel import RWModel


class Food(IDModelMixin, DateTimeModelMixin, RWModel):
    id: int
    name: str
