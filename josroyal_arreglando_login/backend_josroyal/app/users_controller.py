from flask import (
    Blueprint,
    request,
    jsonify,
    abort
)

import jwt
import sys
import datetime
import os

from .models import User
from config.local import config
from .authentication import authorize

users_bp = Blueprint('/users', __name__)


@users_bp.route('/users', methods=['POST'])
def register_user():
        returned_code = 201
        list_errors = []
        try:

            body = request.get_json()

            if 'nickname' not in body:
                list_errors.append('nickname is required')
            else:
                nickname = body.get('nickname')

            if 'e_mail' not in body:
                list_errors.append('e_mail is required')
            else:
                e_mail = body.get('e_mail')

            if 'password' not in body:
                list_errors.append('password is required')
            else:
                password = body.get('password')
            
            if 'confirmationPassword' not in body:
                list_errors.append('confirmationPassword is required')
            else:
                confirmationPassword = body.get('confirmationPassword')

            user = User.query.filter(User.nickname == nickname).first()

            if user is not None:
                if user.nickname == nickname:
                    list_errors.append(
                        'An account with this username already exists')
            else:
                if len(password) < 8:
                    list_errors.append('Password must have at least 8 characters')

                if password != confirmationPassword:
                    list_errors.append(
                        'password and confirmationPassword does not match')

            if len(list_errors) > 0:
                returned_code = 400
            else:
                user = User(nickname, e_mail, password)
                user_created_id = user.insert()

                user_dir = os.path.join('static/usuarios', user.id)
                os.makedirs(user_dir, exist_ok=True)

                file = open(f"{user_dir}/{user.id}.txt", 'w')
                file.close()
                user.skins_hashes = f'{user.id}.txt'

                image_dir = "static/image/persona.jpg"
                user.image = image_dir

                token = jwt.encode({
                'user_created_id': user_created_id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
            }, config['SECRET_KEY'], config['ALGORYTHM'])
            
        except Exception as e:
            print(e)
            print(sys.exc_info())
            returned_code = 500

        if returned_code == 400:
            return jsonify({'success': False, 'message': 'Error creating user', 'errors': list_errors}), returned_code
        elif returned_code != 201:
            abort(returned_code)
        else:
            return jsonify({
            'success': True,
            'token': token,
            'id': user_created_id,
        }), returned_code

@users_bp.route('/users/<user_id>', methods=['PATCH'])
@authorize
def update_user(user_id):
    returned_code = 200
    list_errors = []
    try:

        user = User.query.get(user_id)

        if not user:
            returned_code = 404
        else:

            body = request.json
            new_nick = body.get('nickname')
            balance = body.get('balance')

            if new_nick:
                user.nickname = body['nickname']

            if balance:
                if user.saldo is not None:
                    user.saldo += int(balance)
                else:
                    user.saldo = int(balance)

            user_created_id = user.insert()
                

    except Exception as e:
        print(sys.exc_info())
        returned_code = 500

    if returned_code == 400:
        return jsonify({'success': False, 'message': 'Error updating user'}), returned_code
    elif returned_code != 200:
        abort(returned_code)
    else:
        return jsonify({'success': True, 'message': 'User updated successfully!', 'id': user_created_id}), returned_code


@users_bp.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    returned_code = 200   

    try:
        user = User.query.get(user_id) 
        if user is None:
            returned_code = 404

        user.delete()
    except Exception as e:
        print('\te: ', e)
        returned_code = 500

    if returned_code != 200:
        abort(returned_code)
    else:
        return jsonify({
            'success': True
        })

    

