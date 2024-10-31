import pytest
from app import create_app
from app.db import db
from flask.signals import request_finished
from dotenv import load_dotenv
import os
from app.models.planet import Planet

load_dotenv()


@pytest.fixture
def app():
    test_config = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": os.environ.get("SQLALCHEMY_DATABASE_URI")
    }

    app = create_app(test_config)

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()
    
    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()
    

@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def three_planet_list(app):
    chocolate_topia_planet = Planet(name="Chocolate Topia",
                                    description="A chocolate utopia",
                                    signs_of_life=True)
    swedish_fish_planet = Planet(name="Swedish Fish",
                                description="chocolate, peanut butter, cookie dough galore",
                                signs_of_life=True)
    beet_planet = Planet(name="FRIGGEN BEETS",
                        description="Ew, they don't taste remotely close to corn",
                        signs_of_life=False)
    
    db.session.add_all([chocolate_topia_planet, swedish_fish_planet, beet_planet])
    db.session.commit()




