import allure
import requests as re
from api_clients.base_client import BaseClient
from data.url_endpoints import BASE_URL
from data.url_endpoints import UserEndpoints as UE
from json.decoder import JSONDecodeError


class UserApiClient(BaseClient):
    @allure.step('Create user')
    def create_user(self, username: str, password: str, email: str) -> tuple:
        payload = {
            "email": email, 
            "password": password, 
            "name": username
        }
        resp = self.call_api(*UE.USER_REGISTRATION, data=payload)
        try:
            return resp.status_code, resp.json()
        except JSONDecodeError:
            return resp.status_code, resp.text
        
    @allure.step('Authorization user')
    def authorization_user(self, email: str, password: str) -> tuple:
        payload = {
            "email": email, 
            "password": password
        }
        resp = self.call_api(*UE.USER_LOGIN, json=payload)
        try:
            return resp.status_code, resp.json()
        except JSONDecodeError:
            return resp.status_code, resp.text
        


    @staticmethod
    def create_user_static(username: str, password: str, email: str):
        url = BASE_URL + UE.USER_REGISTRATION[1]
        payload = {
            "email": email, 
            "password": password, 
            "name": username
        }
        resp = re.post(url, data=payload)
        assert resp.status_code < 300, resp.text
        return resp.status_code, resp.json()
    
    @staticmethod
    def login_user_static_return_token(username: str, password: str):
        url = BASE_URL + UE.USER_LOGIN[1]
        payload = {
            "password": password, 
            "name": username
        }
        resp = re.post(url=url, json=payload)
        assert resp.status_code < 300, resp.text
        token = resp.json["accessToken"]
        return token
    
    @staticmethod
    def delete_user_static(accessToken= None, username= None, password= None):
        if accessToken is None:
            assert username == None, "User can't be undefined!"
            assert password == None, "Password can't be undefined!"
            token = UserApiClient.login_user_static_return_token(username,password)
        else: token = accessToken
        headers= {"Authorization": token}
        url = BASE_URL + UE.DELETE_USER[1]
        resp = re.delete(url, headers=headers)
        return resp.status_code