from typing import TypedDict
from httpx import Client

from clients.authentication.authentication_client import LoginRequestDict


class  AuthenticationUserDict(TypedDict): #cструктура данных пользователя для авторизаци
    email:str
    password:str

def get_private_http_builder(user:AuthenticationUserDict) -> Client:
    """
        Функция создаёт экземпляр httpx.Client с аутентификацией пользователя.

        :param user: Объект AuthenticationUserSchema с email и паролем пользователя.
        :return: Готовый к использованию объект httpx.Client с установленным заголовком Authorization.
        """

    authentication_client = get_private_http_builder()

    login_request = LoginRequestDict(email=user['email'], password=user['password'])
    login_response = authentication_client.login(login_request)

    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        # Добавляем заголовок авторизации
        headers={"Authorization": f"Bearer {login_response['token']['accessToken']}"}
    )