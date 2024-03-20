import pytest
from assertpy import assert_that

from server import create_app


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({"TESTING": True, })
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_truck_api_endpoint(client):
    response = client.post("/api/calculate/truck", json={
        "distance_traveled": 100,
        "payload_weight": 100
    }, )

    json_response = response.json
    assert_that(json_response).contains("minutes_spent_refueling")
    assert_that(json_response).contains("number_of_refuels")
    assert_that(json_response).contains("percent_left_in_the_tank")
