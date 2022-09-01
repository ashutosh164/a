import requests
from getpass import getpass


url = 'http://127.0.0.1:8000/auth/'
username = input('Enter username: ')
# password = getpass('Enter password: ')
password = input('Enter password: ')
auth_response = requests.post(url, json={'username': username, 'password': password})
print(auth_response.json())
if auth_response.status_code == 200:
    token = auth_response.json()['token']
    header = {
        'Authorization': f'Token {token}'
    }

    endpoint = 'http://127.0.0.1:8000/details/product/'
    get = requests.get(endpoint, headers=header)
    for i in get.json():
        print(i)

else:
    print('username or password is incorrect')
    print('bad request')


# '2b91e2cbcb5f10c3e69bf3e8654ba0f6d12b427b'


