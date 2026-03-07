import httpx

from httpx import Response

from clients.api_client import APIClient # импортирую класс

from typing import TypedDict # импорт библиотеки для словаря

from clients.private_http_builder import AuthenticationUserDict


class UpdateUserRequest(TypedDict): # писание структуры запроса для обновления пользователя
    email: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None

class PrivateUsersClient(APIClient):  #объявляю новый класс и наследую его от APIClients
    def get_user_me_api(self) -> Response:
        """
        Метод получения текущего пользователя.

        return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("api/v1/users/me")


    def get_user_api(self,user_id:str) -> Response:
        """
        Метод получения пользователя по идентификатору.

        param user_id: Идентификатор пользователя.
        return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"api/v1/users/{user_id}")


    def update_user_api(self, user_id:str, request:UpdateUserRequest) -> Response:
        """
        Метод обновления пользователя по идентификатору.

        param user_id: Идентификатор пользователя.
        param request: Словарь с email, lastName, firstName, middleName.
        return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"api/v1/users/{user_id}", json=request)


    def delete_user_api(self, user_id:str) -> Response:
        """
            Метод удаления пользователя по идентификатору.

            :param user_id: Идентификатор пользователя.
            :return: Ответ от сервера в виде объекта httpx.Response
            """
        return  self.delete(f"api/v1/users/{user_id}")


# Добавляем builder для PrivateUsersClient
def get_private_http_client(user):
    pass


def get_private_users_client(user: AuthenticationUserDict) -> PrivateUsersClient:
    """
    Функция создаёт экземпляр PrivateUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PrivateUsersClient.
    """
    return PrivateUsersClient(client=get_private_http_client(user))