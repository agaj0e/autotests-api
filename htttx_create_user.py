import httpx
from tools.fakers import fake

payload = {
  "email": fake.email(),
  "password": "what",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

create_user = httpx.post('http://127.0.0.1:8000/api/v1/users', json=payload)
print(create_user.json())
print(create_user.status_code)


