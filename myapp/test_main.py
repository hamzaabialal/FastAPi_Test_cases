from fastapi import FastAPI
from fastapi.testclient import TestClient
from fastapi import status
from myapp.main import app

client = TestClient(app)

def test_root():
    response = client.get('/')
    assert response.status_code == status.HTTP_200_OK
    assert response.is_success==True
    assert response.reason_phrase == 'OK'
    assert response.json() == {"message": "Hello World"}

    assert response
def test_get_method():
    response = client.get('/data/', headers={'Accept': 'application/json'})
    assert response.status_code == status.HTTP_200_OK
    assert response.is_success == True
    assert response.reason_phrase == 'OK'
    return response


def test_post_method():
    response = client.post('/data/post/',
                           json={
    "id": 10,
    "name": "I AM  Backend Developerdd",
    "departement": "Bilald",
    "email": "viralvista695@gmail.com",
    "roll_no": 343
})

    assert response.status_code == status.HTTP_201_CREATED

    assert response.reason_phrase == 'Created'

    assert response.json()['name'] == 'Hamza'
    assert response.json()['department'] == 'Biology'
    assert response.json()['email'] == 'hamzaaaabialaal@gmail.com'
    assert response.json()['rol_no'] == 89

    return response

