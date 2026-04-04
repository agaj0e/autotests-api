from httpx import Response
from pydantic import BaseModel, Field

from clients.api_client import  APIClient

class GetExercisesQuerySchema(BaseModel):

    """Описание структуры запроса на получение списка заданий."""
    courseId: str

class CreateExerciseRequestSchema(BaseModel):
    """Описание запросса на создание задания"""

    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExerciseRequestSchema(BaseModel):
    """Описание запроса на обновление задания"""

    title: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class DeleteExerciseSchema(BaseModel):
    """Описание структуры запроса на удаление задания по его ID"""
    courseId: str


class ExercisesClient(APIClient):
    """Клиент для работы с /api/v1/exercises"""

    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """Метод получения списка заданий"""
        return self.client.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id:str) -> Response:
        """Метод получения задания по  его ID"""

        return self.client.get(f"/api/v1/exercises/ {exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Метод создания задания.

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
        Метод обновления задания.

        :param exercise_id: Идентификатор задания.
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления задания.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")
