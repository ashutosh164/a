import requests
endpoint = 'http://127.0.0.1:8000/'
token = '02f2b7ed09d3f3e3b2640a5daad673c5b63288c8'
header = {
    'Authorization': f'Token {token}'
}
data = {
    'title': 'authorization provide for this ',
    'price': 34
}

get_respons = requests.post(endpoint, json=data, headers=header)
print(get_respons.json())

# url = 'http://127.0.0.1:8000/details/product/'
# get = requests.get(url)
# print(get.json())

# n = int(input('enter: '))
# if n >= 1:
#     for i in range(n):
#         print(i ** 2)










