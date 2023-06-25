import json
from unittest.mock import MagicMock

import pytest

from Controller import create_app
from service.PredictionService import PredictionService

app_example = {
    'id': 'abc',
    'text': 'very nice app'
}

test_polarity_data_bad_formed = {
    'dataas': [
        app_example
    ],
    'include': [1, 2, 3]
}

test_polarity_include_bad_formed = {
    'data': [
        app_example
    ],
    'inclsaude': [1, 2, 3]
}

test_polarity_data = {
    'data': [
        app_example
    ],
    'include': [1, 2, 3]
}

test_data_return_scores = {
    'data': [
        app_example
    ],
    'include': []
}

expected_result = [
    app_example
]

test_data_combined = {
    'data': [
        app_example
    ],
    'include-polarity': [1, 2],
    'include-subjectivity': [1, 2]
}

test_data_bad_formed = {
    'include-polarity': [1, 2],
    'include-subjectivity': [1, 2]
}

test_data_combined_miss_pol = {
    'data': [
        app_example
    ],
    'include-subjectivity': [1, 2]
}

test_data_combined_miss_subj = {
    'data': [
        app_example
    ],
    'include-polarity': [1, 2]
}


prediction_service = PredictionService(MagicMock(), MagicMock(), lambda x: x)
prediction_service.predict_polarity = MagicMock(return_value=expected_result)
prediction_service.predict_subjectivity = MagicMock(return_value=expected_result)
prediction_service.predict_both = MagicMock(return_value=expected_result)


@pytest.fixture()
def app():
    app = create_app(prediction_service)
    app.config.update({
        "TESTING": True,
    })
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


def test_infer_polarity_success(app, client):
    response = client.post("/polarity", json=test_polarity_data)
    assert response.status_code == 200
    assert json.loads(response.text) == expected_result


def test_infer_polarity_missing_data(app, client):
    response = client.post("/polarity", json=test_polarity_data_bad_formed)
    assert response.status_code == 400


def test_infer_polarity_missing_include(app, client):
    response = client.post("/polarity", json=test_polarity_include_bad_formed)
    assert response.status_code == 400


def test_infer_subjectivity_success(app, client):
    response = client.post("/subjectivity", json=test_polarity_data)
    assert response.status_code == 200
    assert json.loads(response.text) == expected_result


def test_infer_subjectivity_missing_data(app, client):
    response = client.post("/subjectivity", json=test_polarity_data_bad_formed)
    assert response.status_code == 400


def test_infer_subjectivity_missing_include(app, client):
    response = client.post("/subjectivity", json=test_polarity_include_bad_formed)
    assert response.status_code == 400


def test_infer_polarity_include_scores_success(app, client):
    response = client.post("/polarity", json=test_data_return_scores)
    assert response.status_code == 200
    assert json.loads(response.text) == expected_result

def test_infer_subjectivity_include_scores_success(app, client):
    response = client.post("/subjectivity", json=test_data_return_scores)
    assert response.status_code == 200
    assert json.loads(response.text) == expected_result

def test_infer_both_success(app, client):
    response = client.post("/combined", json=test_data_combined)
    assert response.status_code == 200
    assert json.loads(response.text) == expected_result


def test_infer_both_missing_data(app, client):
    response = client.post("/combined", json=test_data_bad_formed)
    assert response.status_code == 400


def test_infer_both_missing_include_polarity(app, client):
    response = client.post("/combined", json=test_data_combined_miss_pol)
    assert response.status_code == 400


def test_infer_both_missing_include_subjectivity(app, client):
    response = client.post("/combined", json=test_data_combined_miss_subj)
    assert response.status_code == 400
