import allure
from typing import Any,Dict,List
from api_clients.user_api_client import UserApiClient


@allure.feature('Test Login')
class TestLoginUser:

    @allure.title('Login exist user')
    def test_exist_user_success(self, user_api_client_w_user: List[Any|Dict]):
        client: UserApiClient = user_api_client_w_user[0]
        data: Dict = user_api_client_w_user[1]
        resp_code, resp_body = client.authorization_user(email=data["email"], password=data["password"])
        assert resp_code == 200 and resp_body.get("success") and "Bearer" in resp_body.get("accessToken"), \
            f"Responce code: {resp_code}, text: {resp_body}"

    @allure.title('unknown login')
    def test_unknown_user_auth_fail(self, user_api_client_w_user: List[Any|Dict]):
        client: UserApiClient = user_api_client_w_user[0]
        data: Dict = user_api_client_w_user[1]
        resp_code, resp_body = client.authorization_user(email="email@email.com", password=data["password"])
        assert resp_code == 401 and not resp_body.get("success") and \
            resp_body.get("message")=='email or password are incorrect', \
            f"Responce code: {resp_code}, text: {resp_body}"
        
    @allure.title('Incorrect password')
    def test_user_w_wrong_password_auth_fail(self, user_api_client_w_user: List[Any|Dict]):
        client: UserApiClient = user_api_client_w_user[0]
        data: Dict = user_api_client_w_user[1]
        resp_code, resp_body = client.authorization_user(email=data["email"], password="password")
        assert resp_code == 401 and not resp_body.get("success") and \
            resp_body.get("message")=='email or password are incorrect', \
            f"Responce code: {resp_code}, text: {resp_body}"