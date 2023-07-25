
import pytest
import requests
import json


from assertpy import assert_that
from config import BASE_URI
from config import BASE_URI_CLIENT

from utils.print_helpers import pretty_print

@pytest.mark.api
def test_get_client():

    #Act
    response = requests.get(BASE_URI)
    body = response.json()
    pretty_print(body)

    #Assert
    assert response.status_code == 200
    assert 'Python' in body['AbstractText']
    assert_that(response.status_code).is_equal_to(200)

@pytest.mark.api_create_client
def test_create_client():
    userData = {"name": "Tibursio",
                "job": "leader"
    }

    response = requests.post(BASE_URI_CLIENT,
                             json=userData)
    body = response.json()
    assert response.status_code == 201
    assert 'Tibursio' in body['name']
    assert body ["name"] == "Tibursio"

    print(body)
    print(body['name'])
    print("imprime algo por favorrrrrrr!!")