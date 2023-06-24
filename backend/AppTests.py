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

        self.new_invalid_user = {
            'nickname': None,
            'e_mail': '',
            'password':  '1234'
        }

    # Users
    def test_create_user_success(self):
        response = self.client.post('/users', json=self.new_user)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['user']['id'])
        self.user_id = data['user']['id']

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

    def tearDown(self):
        pass
