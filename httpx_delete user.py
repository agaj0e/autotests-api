import httpx

from tools.fakers import random_email

create_user_payload = {
  "email": random_email(),
  "password": "what",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

create_user = httpx.post('http://127.0.0.1:8000/api/v1/users', json=create_user_payload)
create_user_data = create_user.json()

print("Ответ на создание клиента:",create_user_data)

login_payload = {"email":create_user_payload["email"],
                 "password":create_user_payload["password"]}

login_response = httpx.post('http://127.0.0.1:8000/api/v1/authentication/login', json=login_payload)

login_response_data = login_response.json()

print("Ответ сервера на логин:", login_response_data)

delete_headers = {"Authorization": f"Bearer {login_response_data['token']['accessToken']}"}


delete_response = httpx.delete(f'http://127.0.0.1:8000/api/v1/users/{create_user_data['user']['id']}', headers=delete_headers)

delete_response_data = delete_response.json()

print(delete_response.status_code)