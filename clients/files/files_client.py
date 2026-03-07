from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict
from clients.users.private_users_client import get_private_http_client


class CreateFileRequsetDict(TypedDict):
    """Структура запроса на создание файла"""
    filename: str
    directory: str
    upload_file: str


class FilesClient(APIClient):
    """Клиент для работы с эндпоином /api/v1/files """

    def get_file_api(self, file_id:str):
        """Метод получения файла
        """
        return self.get(f'/api/v1/files{file_id}')
    def create_file_api(self,request:CreateFileRequsetDict) -> Response:
        """Метод создания файла
        :param request: Словарь с filename, directory, upload_file.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return  self.post("/api/v1/files",
                          data=request,
                          files={"upload_file":open(request['upload_file'], 'rb')})

    def delete_file_api(self, file_id:str):
        """метод удаления файла"""

        return self.delete(f'/api/v1/files{file_id}')


# Добавляем builder для FilesClient
def get_files_client(user: AuthenticationUserDict) -> FilesClient:
    """
    Функция создаёт экземпляр FilesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию FilesClient.
    """
    return FilesClient(client=get_private_http_client(user))
