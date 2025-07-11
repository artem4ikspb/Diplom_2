import allure
import pytest
from typing import Any,Dict,List
from api_clients.user_api_client import UserApiClient

@allure.feature('Test change user data')
class TestChangeUserData:
    @allure.title('Change userdata')
    @pytest.mark.parametrize(
        'auth_user, change_name, change_password, new_value, code, success',
        [
            (True, False, False, '', 200, True),
            (True, True, False, 'Joe Bidon', 200, True),
            (True, False, True, 'Fagg000t', 200, True),
            (True, True, True, 'PassWord111', 200, True),
            (False, False, False, '', 401, False),
            (False, True, False, 'Donald Trumth', 401, False),
            (False, False, True, 'Magaaaa', 401, False),
            (False, True, True, 'PassWord111', 401, False)
        ],
        ids=[
            'Auth: Change to the same data',
            'Auth: Change name',
            'Auth: Change password',
            'Auth: Change name and password',
            'NoAuth: Change to the same data',
            'NoAuth: Change name',
            'NoAuth: Change password',
            'NoAuth: Change name and password'
        ]
    )
    def test_change_user_data(self, 
                              user_api_client_w_user: List[Any|Dict],
                              auth_user, 
                              change_name, 
                              change_password, 
                              new_value,
                              code, success):
        client: UserApiClient = user_api_client_w_user[0]
        data: Dict = user_api_client_w_user[1]
        token = data['accessToken']
        err_txt = None
        if change_name:
            data['username'] = new_value
        if change_password:
            data['password'] = new_value
        if not auth_user:
            token = None
            err_txt = 'You should be authorised'
        resp_code, resp_body = client.update_user(new_user_data=data,token=token)
        assert resp_code == code and resp_body["success"] == success and resp_body.get("message") == err_txt