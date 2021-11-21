from api.app import app
from flask import json


def test_healthcheck():
    response = app.test_client().get('/health')
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data == {'status': "I'm healthy and wealthy"}


def test_currency_list():
    response = app.test_client().get('/currency')
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data['supported currencies']


def test_currency():
    response = app.test_client().get('/currency/UAH')
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data['data']['currency'] == "UAH"


def test_invalid_currency():
    response = app.test_client().get('/currency/invalid')
    assert response.status_code == 404

