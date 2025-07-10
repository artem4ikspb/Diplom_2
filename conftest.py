import pytest
import data
from api_clients.base_client import BaseClient
from api_clients.user_api_client import UserApiClient as UE
import data.test_data
from data.url_endpoints import BASE_URL
from utils.helpers import Generator

@pytest.fixture(scope="session")
def base_user_api_client():
    client = UE(BASE_URL)    
    yield client
    client.close()

@pytest.fixture(scope="session")
def user_api_client_w_user():
    client = UE(BASE_URL)
    data =  Generator.name(), Generator.password(), Generator.email()
    resp_code, resp_body = UE.create_user_static(*data)
    payload = {
        "username": data[0], 
        "password":data[1], 
        "email": data[2],
        "accessToken": resp_body["accessToken"],
        "resp_code": resp_code,
        "resp_body": resp_body
    }
    yield client, payload
    UE.delete_user_static(accessToken=payload["accessToken"])
    client.close()
