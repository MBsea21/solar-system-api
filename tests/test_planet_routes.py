planet_1_response_body = {"id": 1,
            "name": "Chocolate Topia",
            "description": "A chocolate utopia",
            "signs of life": True}

planet_2_response_body =  {"id": 2,
            "name": "Swedish Fish",
            "description": "chocolate, peanut butter, cookie dough galore",
            "signs of life": True}

planet_3_response_body =  {
            "id": 3,
            "name": "FRIGGEN BEETS",
            "description": "Ew, they don't taste remotely close to corn",
            "signs of life": False}

no_planet_response_body = {"message" : "planet 6 does not exist"}

def test_get_all_planets_empty_records(client):
    response = client.get("/planets")
    response_body = response.get_json()
    print(response_body)

    assert response.status_code == 200
    assert response_body == []

def test_get_all_planets_three_planets(client,three_planet_list):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [planet_1_response_body,planet_2_response_body,planet_3_response_body]

def test_get_one_planet(client,three_planet_list):
    response = client.get("/planets/3")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == planet_3_response_body


def test_get_one_planet_not_found(client,three_planet_list):
    response = client.get("/planets/6")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == no_planet_response_body

def test_post_one_planet(client):
    # before_post_database_response = client.get("/planets")
    # before_post_database_response_body =before_post_database_response.get_json()
    response=client.post("/planets",json={
        "name": "Chocolate Topia",
        "description": "A chocolate utopia!",
        "signs of life": True
        })
    response_body = response.get_json()

    print("actual response", response_body)
    # print("expected response", planet_1_response_body)
    # assert before_post_database_response.status_code == 200
    # assert before_post_database_response_body == []
    assert response.status_code == 201
    assert response_body == {'description': 'A chocolate utopia!', 'id': 1, 'name': 'Chocolate Topia', 'signs of life': True}

    