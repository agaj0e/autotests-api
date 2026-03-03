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


create_file_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"

}


create_file_response = httpx.post('http://127.0.0.1:8000/api/v1/files',
                                  data={"filename":"test_img.png", "directory": "PycharmProjects"},
                                  files={"upload_file": open('testdata/files/test_img.png', 'rb')},
                                  headers=create_file_headers
                                  )

create_file_response_data = create_file_response.json()
print("Ответ на загрузку файла:",create_file_response_data)
print("Статус код:",create_file_response.status_code)
