from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    signs_of_life: Mapped[bool]

    @classmethod
    def from_dict(cls, planet_data):
        new_planet = Planet(
                name=planet_data["name"],
                description=planet_data["description"],
                signs_of_life=planet_data["signs of life"]
                )
        return new_planet

    def to_dict(self):
            return {
                "id": self.id,
                "name": self.name,
                "description": self.description,
                "signs of life": self.signs_of_life
            }


