from flask import Blueprint, abort, make_response
from ..models.planet import planets

planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")

@planet_bp.get("")
def get_all_planets():
    planet_list = []
    for planet in planets: 
        planet_list.append(planet.get_dict())
    return planet_list

@planet_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet=validate_planet(planet_id)
    return planet.get_dict()


def validate_planet(planet_id):
    try: 
        planet_id = int(planet_id)
    except: 
        response = make_response({"message":f"Planet id {planet_id} not valid input type"})
        abort(response, 400)
    for planet in planets:
        if planet.id == planet_id:
            return planet
    response = make_response({"message": f"Planet id {planet_id} not found"})
    abort(response,404)
