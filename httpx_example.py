import httpx

# response = httpx.get('https://jsonplaceholder.typicode.com/todos/1')
#
# print(response.status_code)
# print(response.json())
#
#
# data = {
# "userId": 2,
#   "id": 2,
#   "title": "zalupa rules the world",
#   "completed": True
# }
#
# create_todo = httpx.post("https://jsonplaceholder.typicode.com/todos/", json=data)
#
# print(create_todo.status_code)
# print(create_todo.json())
#
#
#
# with httpx.Client() as client:
#     response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
#     response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")
#     print(response1.json())
#     print(response2.json())

try:
    response = httpx.get("https://jsonplaceholder.typicode.com/invalid_page")
    response.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f"Ошибка запроса: {e}")