from flask import (
    Flask,
    request,
    jsonify,
    abort
)
from .models import db, setup_db, Skin, User, Postventa, Transaccion, Trade
from flask_cors import CORS
from flask_login import login_user, login_required, current_user, LoginManager, UserMixin, logout_user
from .utilities import allowed_file

import os
import sys


def create_app(test_config=None):
    app = Flask(__name__)
    with app.app_context():
        app.config['UPLOAD_FOLDER'] = 'static/usuarios'
        login_manager = LoginManager()
        login_manager.init_app(app)
        app.secret_key = 'clave'
        setup_db(app, test_config['database_path'] if test_config else None)
        CORS(app, origins='*')

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PATCH,POST,DELETE,OPTIONS')
        response.headers.add(' Access-Control-Max-Age', '10')
        return response

    @app.route('/users', methods=['POST'])
    def register_user():
        returned_code = 201
        list_errors = []
        try:

            body = request.json

            if 'nickname' not in body:
                list_errors.append('nickname')
            else:
                nickname = body.get('nickname is required')
            if 'e_mail' not in body:
                list_errors.append('e_mail is required')
            else:
                e_mail = body.get('e_mail')
            if 'password' not in body:
                list_errors.append('password is required')
            else:
                password = body.get('password')

            if len(list_errors) > 0:
                returned_code = 400
            else:
                user = User(nickname, e_mail, password)
                db.session.add(user)
                db.session.commit()

                cwd = os.getcwd()

                user_dir = os.path.join(app.config['UPLOAD_FOLDER'], user.id)
                os.makedirs(user_dir, exist_ok=True)
                upload_folder = os.path.join(cwd, user_dir)

                file = open(f"{user_dir}/{user.id}.txt", 'w')
                file.close()
                user.skins_hashes = f'{user.id}.txt'

                user_id = user.id

        except Exception as e:
            print(e)
            print(sys.exc_info())
            db.session.rollback()
            returned_code = 500
        finally:
            db.session.close()

        if returned_code == 400:
            return jsonify({'success': False, 'message': 'Error creating user', 'errors': list_errors}), returned_code
        elif returned_code != 201:
            abort(returned_code)
        else:
            return jsonify({'success': True, 'message': 'User created successfully!', 'user_id': user_id}), returned_code
