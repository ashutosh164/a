import requests
# admin
# session

url = 'http://127.0.0.1:8000/admin'
get = requests.get(url)
print(get.json())







