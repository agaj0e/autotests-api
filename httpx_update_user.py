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

print(f"Ответ на логин с имеющимися данными:{login_response_data}")


patch_data = {
  "email":random_email(),
  "lastName": "string",
  "firstName": "kkkkaaat",
  "middleName": "string"
}

user_patch_headers = {"Authorization": f"Bearer {login_response_data['token']['accessToken']}"}
user_patch = httpx.patch(f'http://127.0.0.1:8000/api/v1/users/{create_user_data['user']['id']}', json=patch_data, headers=user_patch_headers)

user_patch_data = user_patch.json()
print("Ответ на обновление пользователя:", user_patch_data)
print(user_patch.status_code)

check_patched_user = httpx.get(f'http://127.0.0.1:8000/api/v1/users/{create_user_data['user']['id']}', headers=user_patch_headers)


print('Данные обновленного пользователя',check_patched_user.json())
print(check_patched_user.status_code)

