import requests

url = "https://ammtp.pythonanywhere.com/testapp/get_example"
response = requests.get(url)

print("STATUS: ", response.status_code)
print("RESPONSE: ", response.text)

data = response.json()
print("DATA: ", data)
print("METHOD: ", data["request"]["method"])

assert (data["request"]["path"] == "/testapp/get_example")  # Comprobación de tests

url_post = "https://ammtp.pythonanywhere.com/testapp/post_example"
response_post = requests.post(url_post)

print("STATUS: ", response_post.status_code)
print("RESPONSE: ", response_post.text)

data = response_post.json()
print("DATA: ", data)
print("METHOD: ", data["request"]["method"])

assert (data["request"]["path"] == "/testapp/post_example")  # Comprobación de tests

# Si no se cumple, se rompe la ejecución diciendo qué condición no se cumple

param1 = "1"
param2 = "2"
parametros = {
    'param1': param1,
    'param2': param2
}

response_params = requests.get(url, params=parametros)
assert response_params.json()["request"]["params"]["param1"] == param1
assert response_params.json()["request"]["params"]["param2"] == param2

data = {
    "param1": param1
}
response_data = requests.post(url_post, data=data)
assert response_data.json()["request"]["body"] == ("param1=" + param1)