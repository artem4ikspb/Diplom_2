# Создание заказа:
# с авторизацией,
# без авторизации,
# с ингредиентами,
# без ингредиентов,
# с неверным хешем ингредиентов.
import allure
import pytest
from api_clients.order_api_client import OrderApiClient as order_api
from data.test_data import TestOrderData


@allure.feature("Create order tests")
class TestCreateOrder:
    
    @allure.title("Create order")
    @pytest.mark.parametrize(
        "is_auth_user, ingrs, result_code, is_success",
        [
            (True, TestOrderData.ingredients, 200, True),
            (False, TestOrderData.ingredients, 200, True),
            (True, [], 400, False),
            (True, TestOrderData.bad_ingredients, 400, False)
        ],
        ids=[
            'Auth user',
            'Not auth user',
            'without ingredients',
            'Unknown ingredients'
        ]
    )
    def test_create_order(self, user_api_client_w_user, is_auth_user, ingrs, result_code, is_success):
        token = ''
        if is_auth_user:
            token = user_api_client_w_user[1].get("accessToken")
        resp_code, resp_body = order_api.create_order(ing= ingrs, accessToken= token)
        assert resp_code == result_code and resp_body.get("success") == is_success, f'{resp_body}'