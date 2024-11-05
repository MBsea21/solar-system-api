from app.models.planet import Planet

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
    response = client.post("/planets",json={
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

def test_update_existing_planet(client, three_planet_list):
    test_details = {"name": "Beets R Gross",
                    "description": "ew they are",
                    "signs of life": False}
    response = client.put("/planets/1", json=test_details)

    response_body = response.get_json()
    check_db = client.get("/planets/1")
    check_db_response_body = check_db.get_json()

    assert response.status_code == 200
    assert response_body["message"] == "Planet #1 successfully updated"
    assert check_db.status_code == 200
    assert check_db_response_body["name"] == "Beets R Gross"
    assert check_db_response_body["description"] == "ew they are"
    assert check_db_response_body["signs of life"] == False

def test_update_nonexistent_planet(client, three_planet_list):
    test_details = {"name": "Beets R Gross",
                "description": "ew they are",
                "signs of life": False}
    response = client.put("/planets/6", json=test_details)

    response_body = response.get_json()
    check_db = client.get("/planets/6")

    assert response.status_code == 404
    assert response_body["message"] == "Planet #6 does not exist"
    assert check_db.status_code == 404

def test_update_invalid_planet_id(client, three_planet_list):
    test_details = {"name": "Beets R Gross",
                "description": "ew they are",
                "signs of life": False}
    response = client.put("/planets/cat", json=test_details)

    response_body = response.get_json()
    check_db = client.get("/planets/cat")

    assert response.status_code == 400
    assert response_body["message"] == "Planet #cat is not valid"
    assert check_db.status_code == 400

def test_delete_one_planet(client, three_planet_list):
    response = client.delete("/planets/1")

    response_body = response.get_json()
    check_db = client.get("/planets/1")

    assert response.status_code == 200
    assert response_body["message"] == "Planet #1 successfully deleted"
    assert check_db.status_code == 404

def test_delete_nonexistent_planet(client, three_planet_list):
    response = client.delete("/planets/7")

    response_body = response.get_json()
    check_db = client.get("/planets/7")

    assert response.status_code == 404
    assert response_body["message"] == "Planet #7 does not exist"
    assert check_db.status_code == 404

def test_delete_invalid_planet_id(client, three_planet_list):
    response = client.delete("/planets/dog")

    response_body = response.get_json()
    check_db = client.get("/planets/dog")

    assert response.status_code == 400
    assert response_body["message"] == "Planet #dog is not valid"
    assert check_db.status_code == 400














        



    