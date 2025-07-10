BASE_URL = "https://stellarburgers.nomoreparties.site"

class UserEndpoints:
    USER_REGISTRATION = "POST", "/api/auth/register"
    USER_LOGIN = "POST", "/api/auth/login"
    GET_USER_DATA = "GET", "/api/auth/user"
    UPDATE_USER_DATA = "PATCH", "/api/auth/user"
    DELETE_USER = "DELETE", "/api/auth/user "

class OrderEndpoints:
    CREATE_ORDER = "POST", "/api/orders"