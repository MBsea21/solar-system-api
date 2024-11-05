from flask import abort, make_response
from ..db import db 

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        response = {"message": f"{cls.__name__} #{model_id} is not valid"}
        abort(make_response(response, 400))
    
    query = db.select(cls).where(cls.id == model_id)
    model = db.session.scalar(query)

    if not model:
        response = {"message": f"{cls.__name__} #{model_id} does not exist"}
        abort(make_response(response, 404))

    return model.to_dict()


def create_model(cls, model_data):
    try:
        new_model = cls.from_dict(model_data)
    except KeyError as err:
        response = {"message": f"{cls.__name__} #{err.args[0]} is not valid"}
        abort(make_response(response, 400))

    db.session.add(new_model)
    db.session.commit()

    return new_model.to_dict(), 201


