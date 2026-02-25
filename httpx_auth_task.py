import httpx

payload = {
  "email": "zalupa666@example.com",
  "password": "zalupa"
}


login = httpx.post('http://127.0.0.1:8000/api/v1/authentication/login', json=payload)

login_response = login.json()
print(login.status_code)
print(login_response)

access_token = {
    "Authorization": f"Bearer {login_response['token']['accessToken']}"
}

getUserMe = httpx.get('http://127.0.0.1:8000/api/v1/me', headers=access_token)

getUserMe_response = getUserMe.json()
print(getUserMe_response)

