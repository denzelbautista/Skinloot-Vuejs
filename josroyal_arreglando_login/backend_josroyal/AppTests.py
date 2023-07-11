import unittest  # libreria de python para realizar test
from config.qa import config
from app.models import User, Skin
from app import create_app
from flask_sqlalchemy import SQLAlchemy
import json
import random
import string
import io as io


def random_email(char_num):
    return ''.join(random.choice(string.ascii_lowercase)
                   for _ in range(char_num)) + "@gmail.com"

def random_username(char_num):
    return ''.join(random.choice(string.ascii_lowercase)
                   for _ in range(char_num))

class SkinlootTests(unittest.TestCase):
    def setUp(self):
        database_path = config['DATABASE_URI']
        self.app = create_app({'database_path': database_path})
        self.client = self.app.test_client()

        self.add_c_user_cash = {
            'balance' : '50'
        }

        self.new_invalid_user = {
            'nickname': None,
            'e_mail': '',
            'password':  '1234'
        }

        self.new_skin = {
            'name': 'Gragas_camorrista',
            'champion_name': 'Gragas',
            'rarity': 'Normal',
            'user_id': ' '
        }

        self.new_skin_failed = {
            'name': 'test_fail',
            'champion_name': 'test_fail',
            'rarity': 'Normal',
            'user_id': '615sd5sas6515c15as-as5da1s5d5as'
        }

        self.new_post = {
            'title': 'TestPost',
            'skin_id': ' ',
            'name': 'Gragas_camorrista',
            'champion': 'Gragas',
            'price': '19'
        }

        self.new_invalid_post = {
            'title': None,
            'skin_id': ' ',
            'name': 'Gragas_camorrista',
            'champion': 'Gragas',
            'price': '19'
        }

        self.new_sell = {
            'skin_uid': ' ',
            'seller_uid': ' ',
            'price': '19',
            'post_id': ' ',
        }

        self.new_authenticated_user = {
            'nickname': random_username(10),
            'e_mail': random_email(7),
            'password': '147258369',
            'confirmationPassword': '147258369'
        }

        self.new_c_user = {
            'nickname': random_username(10),
            'e_mail': random_email(7),
            'password': '147258369',
            'confirmationPassword': '147258369'
        }

        response_user = self.client.post(
            '/users', json=self.new_authenticated_user)
        data_user = json.loads(response_user.data)
        self.user_valid_token = data_user['token']
        self.user_created_id = data_user['id']

        self.headers = {
            "content-type": 'application/json'
        }

        response_user_c = self.client.post(
            '/users', json=self.new_c_user)
        data_user_c = json.loads(response_user_c.data)
        self.user_c_valid_token = data_user_c['token']
        self.user_c_created_id = data_user_c['id']

        self.headers_c = {
            "content-type": 'application/json'
        }

    # Skins
    def test_create_skin_success(self):
        self.headers['X-ACCESS-TOKEN'] = self.user_valid_token
        self.new_skin['user_id'] = str(self.user_created_id)
        
        response = self.client.post('/skins', json=self.new_skin, headers=self.headers)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['skin']['id'])

    def test_create_skin_failed_400(self):
        self.headers['X-ACCESS-TOKEN'] = self.user_valid_token
        response = self.client.post('/skins', json={}, headers=self.headers)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])

    def test_create_skin_failed_500(self):
        self.headers['X-ACCESS-TOKEN'] = self.user_valid_token
        response = self.client.post('/skins', json=self.new_skin_failed, headers=self.headers)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 500)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])

    # Posts
    def test_create_post_success(self):
        self.headers['X-ACCESS-TOKEN'] = self.user_valid_token
        self.new_skin['user_id'] = str(self.user_created_id)

        response_skin_tmp = self.client.post('/skins', json=self.new_skin, headers=self.headers)
        data_skin_tmp = json.loads(response_skin_tmp.data)
        skin_tmp_id = data_skin_tmp['skin']['id']
        self.new_post['skin_id'] = str(skin_tmp_id)

        response = self.client.post(
            '/posts/{}'.format(self.user_created_id), json=self.new_post, headers=self.headers)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['message'])
    
    def test_create_post_failed_400(self):
        self.headers['X-ACCESS-TOKEN'] = self.user_valid_token

        response = self.client.post(
            '/posts/{}'.format(self.user_created_id), json={}, headers=self.headers)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])

    def test_create_post_failed_500(self):
        self.headers['X-ACCESS-TOKEN'] = self.user_valid_token
        self.new_skin['user_id'] = str(self.user_created_id)

        response_skin_tmp = self.client.post('/skins', json=self.new_skin, headers=self.headers)
        data_skin_tmp = json.loads(response_skin_tmp.data)
        skin_tmp_id = data_skin_tmp['skin']['id']
        self.new_invalid_post['skin_id'] = str(skin_tmp_id)

        response = self.client.post(
            '/posts/{}'.format(self.user_created_id), json=self.new_invalid_post, headers=self.headers)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])
    
    # Sells
    def test_buy_skin_success(self):
        self.headers_c['X-ACCESS-TOKEN'] = self.user_c_valid_token
        self.headers['X-ACCESS-TOKEN'] = self.user_valid_token

        # vamos a usar patch para agregar saldo al user_c
        response_new_cash = self.client.patch('/users/{}'.format(self.user_c_created_id), json=self.add_c_user_cash, headers=self.headers_c)
        data_new_cash = json.loads(response_new_cash.data)
        user_c_new_cash_id = data_new_cash['id']

        self.new_skin['user_id'] = str(self.user_created_id)
        self.new_sell['seller_uid'] = str(self.user_created_id)

        response_skin_tmp = self.client.post('/skins', json=self.new_skin, headers=self.headers)
        data_skin_tmp = json.loads(response_skin_tmp.data)
        skin_tmp_id = data_skin_tmp['skin']['id']
        self.new_post['skin_id'] = str(skin_tmp_id)
        self.new_sell['skin_uid'] = str(skin_tmp_id)

        response_post_tmp = self.client.post(
            '/posts/{}'.format(self.user_created_id), json=self.new_post, headers=self.headers)
        data_post_tmp = json.loads(response_post_tmp.data)
        post_tmp_id = data_post_tmp['post']['id']
        self.new_sell['post_id'] = str(post_tmp_id)

        response = self.client.post('/users/{}/skins'.format(user_c_new_cash_id), json=self.new_sell, headers=self.headers_c)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['message'])
    

    def tearDown(self):
        self.client.delete('/users/{}'.format(self.user_created_id))
        self.client.delete('/users/{}'.format(self.user_c_created_id))
