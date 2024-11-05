from flask import Blueprint, abort, make_response, request, Response
from ..models.planet import Planet
from ..db import db
from ..routes.route_utilities import validate_model as validate_planet, create_model

planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")

@planet_bp.post("")
def create_planet():
    request_body = request.get_json()

    return create_model(Planet, request_body)


@planet_bp.get("")
def get_planets():

    query = db.select(Planet)

    name_param = request.args.get("name")
    if name_param:
        print(name_param)
        query = query.where(Planet.name.ilike(f"%{name_param}%"))
        print(query)

    description_param = request.args.get("description")
    if description_param:
        query = query.where(Planet.description.ilike(f"%{description_param}%"))

    life_param = request.args.get("signs of life")
    if life_param:
        query = query.where(Planet.signs_of_life.ilike(f"%{life_param}%"))

    sort_param = request.args.get("sort")
    print(type(sort_param))
    print(type(Planet.name))


    if sort_param == "name":
        query = query.order_by(Planet.name)
    elif sort_param == "description":
        query = query.order_by(Planet.description)
    elif sort_param == "signs of life":
        query = query.order_by(Planet.signs_of_life)
    else:
        query = query.order_by(Planet.id)

    planets = db.session.scalars(query)

    planets_response = [planet.to_dict() for planet in planets]
    return planets_response

@planet_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_planet(Planet, planet_id)
    
    return planet

@planet_bp.put("/<planet_id>")
def update_planet(planet_id):
    planet = validate_planet(Planet, planet_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.signs_of_life = request_body["signs of life"]

    db.session.commit()
    return Response(status=204, mimetype="application/json")


@planet_bp.delete("/<planet_id>")
def delete_planet(planet_id):
    planet = validate_planet(Planet, planet_id)

    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype="application/json")

