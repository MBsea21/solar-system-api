from flask import Blueprint
from ..models.planet import planets

planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")

@planet_bp.get("")
def get_all_planets():
    planet_list = []
    for planet in planets: 
        planet_list.append( {
            "id" : planet.id,
            "name" : planet.name,
            "description" : planet.description,
            "signs of life" : planet.signs_of_life

        })
    return planet_list