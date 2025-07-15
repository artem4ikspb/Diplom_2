import allure
import requests as re
from typing import List
from api_clients.base_client import BaseClient
from api_clients.user_api_client import UserApiClient
from data.url_endpoints import BASE_URL
from data.url_endpoints import OrderEndpoints as OE
from data.test_data import TestOrderData as Ing
from json.decoder import JSONDecodeError


class OrderApiClient:

    @staticmethod
    def create_order(ing: List[str], accessToken= None, username= None, password= None):
        url = BASE_URL + OE.CREATE_ORDER[1]
        if accessToken is None:
            assert username == None, "User can't be undefined!"
            assert password == None, "Password can't be undefined!"
            token = UserApiClient.login_user_static_return_token(username,password)
        else: token = accessToken
        headers= {"Authorization": token}
        payload = {"ingredients": ing}
        resp = re.post(url=url, data=payload)
        try:
            return resp.status_code, resp.json()
        except JSONDecodeError:
            return resp.status_code, resp.text        


    @staticmethod
    def get_user_orders(accessToken):
        url = BASE_URL + OE.GET_USER_ORDERS[1]
        headers= {"Authorization": accessToken}
        resp = re.get (url=url, headers=headers)
        try:
            return resp.status_code, resp.json()
        except JSONDecodeError:
            return resp.status_code, resp.text 