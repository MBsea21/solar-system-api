from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    signs_of_life: Mapped[bool]

    def get_dict(self):
            return {
                "id": self.id,
                "name": self.name,
                "description": self.description,
                "signs of life": self.signs_of_life
            }


