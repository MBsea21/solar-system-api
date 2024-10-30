from flask import Blueprint, abort, make_response, request, Response
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


# create description query and name query and signs of life query
# create order by (sort) query
# test the requests



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
    planet = validate_planet(planet_id)
    response = planet.to_dict()
    # response = {
    #     "id": planet.id,
    #     "name": planet.name,
    #     "description": planet.description,
    #     "signs of life": planet.signs_of_life 
    # }
    return response




def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except: 
        response = ({"message": f"planet {planet_id} invalid"},400)
        abort(make_response(response))
    
    query = db.select(Planet).where(Planet.id == planet_id)
    planet = db.session.scalar(query)

    if not planet:
        response = ({"message" : f"planet {planet_id} does not exist"}, 404)
        abort(make_response(response))

    return planet

@planet_bp.put("/<planet_id>")
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.signs_of_life = request_body["signs of life"]

    db.session.commit()
    return Response(status=204, mimetype="application/json")


@planet_bp.delete("/<planet_id>")
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype="application/json")

