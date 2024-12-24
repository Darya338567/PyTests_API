import os.path

from api_1 import Pets
pt = Pets()

def test_get_token():
    status = pt.get_token()[1]
    assert status == 200


def test_get_list_users():
    status = pt.get_list_users()[0]
    amount = pt.get_list_users()[1]
    assert status == 200
    assert amount


def test_post_pet():
    status = pt.post_pet()[1]
    pet_id = pt.post_pet()[0]
    assert status == 200
    assert pet_id


def test_get_pet_photo(pet_photo='tests\\photo\\pet.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    status = pt.get_pet_photo()[0]
    assert status == 200
    assert pet_photo

def test_get_pet_like():
    status = pt.get_pet_like()[0]
    assert status == 200

def test_delete_pet():
    status = pt.delete_pet()[1]
    pet_id = pt.delete_pet()[0]
    assert status == 200
    assert pet_id

def test_patch_pet():
    status = pt.patch_pet()[1]
    pet_id = pt.patch_pet()[0]
    assert status == 200
    assert pet_id

def test_get_pet():
    status = pt.get_pet()[0]
    pet_id = pt.get_pet()[1]
    assert status == 200
    assert pet_id


