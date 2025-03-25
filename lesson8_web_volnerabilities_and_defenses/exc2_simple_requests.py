import requests
import json

def get():
    response = requests.get("http://httpbin.org/status/204")
    return response.status_code

def post():
    data = {'x': 1, 'y': 2}
    response = requests.post("http://httpbin.org/post", data=data)
    return response
