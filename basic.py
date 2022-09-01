import requests

# endpoint = 'http://127.0.0.1:8000/'

# get_responce = requests.post(endpoint, json={'title': 'Hello Ashutosh'})
# # print(get_responce.text)
#
# print(get_responce.json())
# print(get_responce.status_code)


'''details test'''
endpoint = 'http://127.0.0.1:8000/'

get_respons = requests.get(endpoint)
# print(get_respons.json())
# for i in get_respons.json():
#     print(i)
'''create test'''
# endpoint = 'http://127.0.0.1:8000/create/'
# get_respons = requests.post(endpoint)
# print(get_respons.json())


url = 'http://127.0.0.1:8000/details/8/'
get = requests.get(url)
print(get.json())


create = 'http://127.0.0.1:8000/details/product'
post = requests.post(create, json={'title': 'Hello Ashutosh'})
# print(post.json())

'''update'''

urls = 'http://127.0.0.1:8000/details/8/update/'
data = {
    'title': 'python',
    'content': 'i love coding',
    'price': 120.99
}

up = requests.put(urls, json=data)
# print(up.json())


dl_url = 'http://127.0.0.1:8000/details/8/update/'

id = input('what product id you want to use: ')
try:
    id = int(id)
except:
    id = None
    print(f'{id} not a valid id')

if id:
    dl_url = 'http://127.0.0.1:8000/details/{id}/delete/'

    dl = requests.delete(dl_url)
    print(dl.status_code, get_respons.status_code==204)

