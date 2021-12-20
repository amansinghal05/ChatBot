import requests

url = "http://localhost:8080/weather"
param = {
    "city_name": ""
}
response = requests.put(url, params=param)
print(response.text)