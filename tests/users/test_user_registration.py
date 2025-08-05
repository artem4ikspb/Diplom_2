import allure
import pytest
from api_clients.user_api_client import UserApiClient as UE

@allure.feature('Test registration user')
class TestUserRegistration:

    @allure.title('Create user')
    def test_create_user_valid(self, user_api_client_w_user):
        assert user_api_client_w_user[1]["resp_code"] == 200 and user_api_client_w_user[1]["resp_body"]["success"]

    @allure.title('Create exist user')
    def test_create_exist_user_fail(self, user_api_client_w_user):
        data = user_api_client_w_user[1]
        resp_code, resp_body = user_api_client_w_user[0].create_user(
            username=data["username"],
            password=data["password"],
            email=data["email"]
        )
        assert resp_code == 403 and not resp_body["success"] \
            and resp_body["message"] == "User already exists"

    @allure.title('Try to create user without mandatory fields')
    @pytest.mark.parametrize(
        'fields',
        [
            ['','fdsdfd908098','fdsdfd908098@yabgd.ru'],
            ['fdsdfd908098','','fdsdfd908098@yabgd.ru'],
            ['fdsdfd908098','fdsdfd908098',''],
            [None,'fdsdfd908098','fdsdfd908098@yabgd.ru'],
            ['fdsdfd908098',None,'fdsdfd908098@yabgd.ru'],
            ['fdsdfd908098','fdsdfd908098',None]
        ]
    )
    def test_create_user_wo_mandatory_fields(seld, base_user_api_client, fields):
        resp_code, resp_body = base_user_api_client.create_user(
            username=fields[0],
            password=fields[1],
            email=fields[2]
        )
        assert resp_code == 403 and not resp_body["success"] \
            and resp_body["message"] == "Email, password and name are required fields"
