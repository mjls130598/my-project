import requests

body = {
    "a": "1",
    "b": "2"
}
response = requests.post("http://127.0.0.1:8080/post_suma", json=body)

print(response.text)

assert response.json()["resultado"] == 3

body = '''{
    "a": "1",
    "b": "2"
}'''

response = requests.post("http://127.0.0.1:8080/post_suma", data=body)

print(response.text)

assert response.json()["resultado"] == 3