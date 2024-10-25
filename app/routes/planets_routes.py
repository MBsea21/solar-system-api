from flask import Blueprint, abort, make_response, request
from ..models.planet import Planet
from ..db import db

planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")

@planet_bp.post("")
def create_planet():
    request_body = request.get_json()
    name = request_body["name"]
    description = request_body["description"]
    signs_of_life = request_body["signs of life"]

    new_planet = Planet(name=name, description=description, signs_of_life=signs_of_life)
    db.session.add(new_planet)
    db.session.commit()

    response = {
        "id": new_planet.id,
        "name": new_planet.name,
        "description": new_planet.description,
        "signs of life": new_planet.signs_of_life
    }

    return response, 201


@planet_bp.get("")
def get_planets():
    query = db.select(Planet).order_by(Planet.id)
    planets = db.session.scalars(query)

    planets_response = [planet.get_dict() for planet in planets]
    return planets_response
