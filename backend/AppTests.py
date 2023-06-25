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


class SkinlootTests(unittest.TestCase):
    def setUp(self):
        database_path = config['DATABASE_URI']
        self.app = create_app({'database_path': database_path})
        self.client = self.app.test_client()

        self.new_user = {
            'nickname': 'test',
            'e_mail': random_email(7),
            'password':  '1234'
        }

        self.new_c_user = {
            'nickname': 'shopperuser',
            'e_mail': random_email(7),
            'password':  '12345'
        }

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


    # Users
    def test_create_user_success(self):
        response = self.client.post('/users', json=self.new_user)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['user']['id'])

    def test_create_user_failed_400(self):
        response = self.client.post('/users', json={})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])

    def test_create_user_failed_500(self):
        response = self.client.post('/users', json=self.new_invalid_user)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 500)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])

    # Skins
    def test_create_skin_success(self):
        response_user_temp = self.client.post('/users', json=self.new_user)
        data_tmp = json.loads(response_user_temp.data)
        user_temp_id = data_tmp['user']['id']
        self.new_skin['user_id'] = str(user_temp_id)

        response = self.client.post('/skins', json=self.new_skin)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['skin']['id'])

    def test_create_skin_failed_400(self):
        response = self.client.post('/skins', json={})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])

    def test_create_skin_failed_500(self):
        response = self.client.post('/skins', json=self.new_skin_failed)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 500)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])

    # Posts
    def test_create_post_success(self):
        response_user_temp = self.client.post('/users', json=self.new_user)
        data_tmp = json.loads(response_user_temp.data)
        user_temp_id = data_tmp['user']['id']
        self.new_skin['user_id'] = str(user_temp_id)

        response_skin_tmp = self.client.post('/skins', json=self.new_skin)
        data_skin_tmp = json.loads(response_skin_tmp.data)
        skin_tmp_id = data_skin_tmp['skin']['id']
        self.new_post['skin_id'] = str(skin_tmp_id)

        response = self.client.post(
            '/posts/{}'.format(user_temp_id), json=self.new_post)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['message'])
    
    def test_create_post_failed_400(self):
        response_user_temp = self.client.post('/users', json=self.new_user)
        data_tmp = json.loads(response_user_temp.data)
        user_temp_id = data_tmp['user']['id']
        self.new_skin['user_id'] = str(user_temp_id)

        response_skin_tmp = self.client.post('/skins', json=self.new_skin)
        data_skin_tmp = json.loads(response_skin_tmp.data)
        skin_tmp_id = data_skin_tmp['skin']['id']
        self.new_post['skin_id'] = str(skin_tmp_id)

        response = self.client.post(
            '/posts/{}'.format(user_temp_id), json={})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])

    def test_create_post_failed_500(self):
        response_user_temp = self.client.post('/users', json=self.new_user)
        data_tmp = json.loads(response_user_temp.data)
        user_temp_id = data_tmp['user']['id']
        self.new_skin['user_id'] = str(user_temp_id)

        response_skin_tmp = self.client.post('/skins', json=self.new_skin)
        data_skin_tmp = json.loads(response_skin_tmp.data)
        skin_tmp_id = data_skin_tmp['skin']['id']
        self.new_invalid_post['skin_id'] = str(skin_tmp_id)

        response = self.client.post(
            '/posts/{}'.format(user_temp_id), json=self.new_invalid_post)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])
    
    # Sells
    def test_buy_skin_success(self):
        response_user_c_temp = self.client.post('/users', json=self.new_c_user)
        data_c_tmp = json.loads(response_user_c_temp.data)
        user_c_temp_id = data_c_tmp['user']['id']

        # vamos a usar patch para agregar saldo al user_c
        response_new_cash = self.client.patch('/users/{}'.format(user_c_temp_id), json=self.add_c_user_cash)
        data_new_cash = json.loads(response_new_cash.data)
        user_c_new_cash_id = data_new_cash['id']

        response_user_temp = self.client.post('/users', json=self.new_user)
        data_tmp = json.loads(response_user_temp.data)
        user_temp_id = data_tmp['user']['id']
        self.new_skin['user_id'] = str(user_temp_id)
        self.new_sell['seller_uid'] = str(user_temp_id)

        response_skin_tmp = self.client.post('/skins', json=self.new_skin)
        data_skin_tmp = json.loads(response_skin_tmp.data)
        skin_tmp_id = data_skin_tmp['skin']['id']
        self.new_post['skin_id'] = str(skin_tmp_id)
        self.new_sell['skin_uid'] = str(skin_tmp_id)

        response_post_tmp = self.client.post(
            '/posts/{}'.format(user_temp_id), json=self.new_post)
        data_post_tmp = json.loads(response_post_tmp.data)
        post_tmp_id = data_post_tmp['post']['id']
        self.new_sell['post_id'] = str(post_tmp_id)

        response = self.client.post('/users/{}/skins'.format(user_c_new_cash_id), json=self.new_sell)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['message'])
    

    def tearDown(self):
        pass
