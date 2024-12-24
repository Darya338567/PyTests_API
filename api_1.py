import json
import requests

from requests_toolbelt.multipart.encoder import MultipartEncoder
from settings import VALID_EMAIL, VALID_PASSWORD


class Pets:
    """ API библиотека к сайту http://34.141.58.52:8080/#/"""

    def __init__(self):
        self.base_url = 'http://34.141.58.52:8000/'

    def get_registered(self) -> json:
        data = {"email": VALID_EMAIL,
                "password": VALID_PASSWORD, "confirm_password": VALID_PASSWORD}
        res = requests.post(self.base_url + 'register', data=json.dumps(data))
        my_id = res.json()
        my_id = my_id.get('id')
        status = res.status_code
        print(my_id)
        return status, my_id

    def get_token(self) -> json:
        """Запрос к Swagger сайта для получения уникального токена пользователя по указанным email и password"""
        data = {"email": VALID_EMAIL,
                "password": VALID_PASSWORD}
        res = requests.post(self.base_url + 'login', data=json.dumps(data))
        my_token = res.json()['token']
        my_id = res.json()['id']
        status = res.status_code
        print(my_token)
        print(res.json())
        return my_token, status, my_id

    def get_list_users(self):
        my_token = Pets().get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + 'users', headers=headers)
        status = res.status_code
        my_id = res.text

        print(res.json())
        return status, my_id

    def post_pet(self):
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[2]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": my_id,
                "name": 'Chip', "type": 'dog', "age": 47, "owner_id": my_id}
        res = requests.post(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        pet_id = res.json()['id']
        status = res.status_code
        print(pet_id)
        print(res.json())
        return pet_id, status

    def get_pet_photo(self):
        my_token = Pets().get_token()[0]
        pet_id = Pets().post_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        pic = open('tests\\photo\\pet.jpg', 'rb')
        #files = {'pic': ('что-угодно.jpg', open('tests\\photo\\pet.jpg', 'rb'), 'image/jpg')}

        res = requests.post(self.base_url + f'pet/{pet_id}/image', headers=headers, files=pic)
        status = res.status_code
        link = res.json()['link']
        print(res.json())
        return status, link

    def get_pet_like(self):
        my_token = Pets().get_token()[0]
        #pet_id = Pets().get_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": 557}
        res = requests.put(self.base_url + f'pet/{557}/like', data=json.dumps(data), headers=headers)
        status = res.status_code
        print(res.json())
        print(status)
        return status

    def delete_pet(self):
        """Запрос на удаление питомца заданного id"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().post_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.delete(self.base_url + 'pet' + f'{pet_id}', headers=headers)
        pet_id = res.json()['id']
        status = res.status_code
        print(pet_id)
        print(res.json())
        return pet_id, status

    def patch_pet(self):
        """Запрос на частичное обновление данных питомца"""
        my_token = Pets().get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": 32552,
                "name": "Kuzja",
                "type": "dog",
                "age": 8,
                "gender": "male",
                "owner_id": 0,
                "pic": "string",
                "owner_name": "Darya",
                "likes_count": 5,
                "liked_by_user": False}
        res = requests.patch(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        pet_id = res.json()['id']
        status = res.status_code
        print(pet_id)
        print(res.json())
        return pet_id, status

    def get_pet(self):
        """Запрос на получение данных питомца по заданному id питомца"""
        my_token = Pets().get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        pet_id = Pets().post_pet()[0]
        res = requests.get(self.base_url + 'pet' + f'{pet_id}', headers=headers)
        pet_id = res.json()['id']
        status = res.status_code
        print(res.json())
        return status, pet_id


Pets().get_registered()
Pets().get_token()
Pets().get_list_users()
Pets().post_pet()
Pets().get_pet_photo()
Pets().get_pet_like()
Pets().delete_pet()
Pets().patch_pet()
Pets().get_pet()
