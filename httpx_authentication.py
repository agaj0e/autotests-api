import httpx

payload = {
  "email": "zalupa666@example.com",
  "password": "zalupa"
}

login_response = httpx.post('http://127.0.0.1:8000/api/v1/authentication/login', json=payload)
login_reponse_data = login_response.json()

print("login response", login_reponse_data)
print(login_response.status_code)

refresh_payload = {
  "refreshToken": login_reponse_data['token']['refreshToken']
}

refresh_response = httpx.post('http://127.0.0.1:8000/api/v1/authentication/refresh', json=refresh_payload)
refresh_response_data = refresh_response.json()

print("refresh response", refresh_response_data)
print(refresh_response.status_code)
