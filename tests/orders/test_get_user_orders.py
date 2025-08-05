# Получение заказов конкретного пользователя:
# авторизованный пользователь,
# неавторизованный пользователь.


import allure
import pytest
from typing import Any,Dict,List
from api_clients.order_api_client import OrderApiClient as order_api


@allure.feature('Get user orders')
class TestGetUserOrders:

    @allure.title('Get user orders')
    @pytest.mark.parametrize(
        "is_auth_user, result_code, is_success",
        [
           (True, 200, True),
           (False, 401, False)
        ]
    )
    def test_get_user_orders(self, user_api_client_w_user, is_auth_user, result_code, is_success):
        token = ''
        if is_auth_user:
            token = user_api_client_w_user[1].get("accessToken")
        resp_code, resp_body = order_api.get_user_orders(token)
        assert resp_code == result_code and resp_body.get("success") == is_success, f'{resp_body}'