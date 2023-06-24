from flask import (Flask, request, jsonify, abort)
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

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route('/users', methods=['POST'])
    def register_user():
        returned_code = 201
        list_errors = []
        try:

            body = request.json

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

                # image_dir = os.path.join("static/image/persona.jpg")
                image_dir = "static/image/persona.jpg"
                user.image = image_dir
                db.session.commit()
                login_user(user)
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
            return jsonify({'success': True, 'message': 'User created successfully!', 'user': user.serialize()}), returned_code

    @app.route('/users/<user_id>', methods=['PATCH'])
    def update_user(user_id):
        returned_code = 200
        list_errors = []
        try:

            user = User.query.filter_by(id=user_id).first()

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

                db.session.commit()
                user_id = user.id

        except Exception as e:
            print(sys.exc_info())
            db.session.rollback()
            returned_code = 500
        finally:
            db.session.close()

        if returned_code == 400:
            return jsonify({'success': False, 'message': 'Error updating user'}), returned_code
        elif returned_code != 200:
            abort(returned_code)
        else:
            return jsonify({'success': True, 'message': 'User updated successfully!', 'id': user_id}), returned_code

    @app.route('/skins', methods=['POST'])
    def register_skins():
        returned_code = 201
        list_errors = []
        try:
            body = request.json
            if 'name' not in body:
                list_errors.append('name is required')
            else:
                name = body.get('name')
            if 'champion_name' not in body:
                list_errors.append('champion_name is required')
            else:
                champion_name = body.get('champion_name')
            if 'rarity' not in body:
                list_errors.append('rarity is required')
            else:
                rarity = body.get('rarity')
            if 'user_id' not in body:
                list_errors.append('user_id is required')
            else:
                user_id = body.get("user_id")

            if len(list_errors) > 0:
                returned_code = 400
            else:
                skin = Skin(name, champion_name, rarity, user_id)
                db.session.add(skin)
                db.session.commit()
                uid = skin.id

                filename = f'{user_id}.txt'
                filepath = os.path.join(
                    f"{app.config['UPLOAD_FOLDER']}/{user_id}", filename)

                with open(filepath, 'a') as file:
                    file.write(str(uid) + '\n')
                file.close()

            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return jsonify({'success': False, 'error': str(e)})
        finally:
            db.session.close()
        if returned_code == 400:
            return jsonify({'success': False, 'message': "Error creating skin", 'errors': list_errors}), returned_code
        elif returned_code != 201:
            abort(returned_code)
        else:
            return jsonify({'success': True, 'message': "skin created successfully!", 'skin_id': uid}), returned_code

    @app.route('/show-skins-current/<user_id>', methods=['GET'])
    def current_skins(user_id):
        try:
            skins = Skin.query.filter_by(user_id=user_id).all()
            skins_serialized = [skin.serialize() for skin in skins]
            return jsonify({'success': True, "serialize": skins_serialized})
        except Exception as e:
            return jsonify({'success': False, "error": str(e)})

    @app.route('/show-posts', methods=['GET'])
    def showPosts():
        try:
            posts = Postventa.query.filter_by(on_sale=True).all()
            posts_serialized = [post.serialize() for post in posts]
            return jsonify({'success': True, 'serialized': posts_serialized})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})

    @app.route('/show-skins', methods=['GET'])
    def showSkins():
        try:
            skins = Skin.query.all()
            skins_serialized = [skin.serialize() for skin in skins]
            return jsonify({'success': True, 'skins': skins_serialized})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})

    @app.route('/post-venta/<user_id>', methods=['POST'])
    def create_postventa(user_id):
        returned_code = 201
        list_errors = []
        try:
            body = request.json
            if 'title' not in body:
                list_errors.append('title is required')
            else:
                title = body.get('title')
            if 'skin_id' not in body:
                list_errors.append('skin_id is required')
            else:
                skin_id = body.get('skin_id')
            if 'name' not in body:
                list_errors.append('name is required')
            else:
                name = body.get('name')
            if 'price' not in body:
                list_errors.append('price is required')
            else:
                price = body.get('price')
            if 'champion' not in body:
                list_errors.append('champion is required')
            else:
                champion = body.get('champion')

            if len(list_errors) > 0:
                returned_code = 400
            else:
                user_id = user_id
                skin_image = os.path.join(
                    "static/campeones", f'{champion}', f'{name}.jpg')
                on_sale = True
                skin = Skin.query.get(skin_id)
                if not skin:
                    return jsonify({'success': False, 'message': 'Skin not found'})
                postventa = Postventa(title, user_id, skin_id, on_sale, int(
                    price), champion, skin_image, name)
                db.session.add(postventa)
                db.session.commit()

                return jsonify({'success': True, 'title': title, 'user_id': user_id, 'skin_id': skin_id, 'champion': champion, 'skin_image': skin_image, 'on_sale': on_sale})
        except Exception as e:
            return jsonify({'success': False, 'message': str(e)})
        finally:
            db.session.close()

    @app.route('/comprar-skin/<user_id>', methods=['POST'])
    def comprar_skin(user_id):
        returned_code = 201
        list_errors = []
        try:
            body = request.json
            if 'skin_uid' not in body:
                list_errors.append('skin_uid is required')
            else:
                skin_uid = body.get('skin_uid')
            if 'seller_uid' not in body:
                list_errors.append('seller_uid is required')
            else:
                seller_uid = body.get('seller_uid')
            if 'price' not in body:
                list_errors.append('price is required')
            else:
                price = body.get('price')
            if 'post_id' not in body:
                list_errors.append('post_id is required')
            else:
                post_id = body.get('post_id')

            if len(list_errors) > 0:
                returned_code = 400
            else:
                posteo = Postventa.query.filter_by(id=post_id).first()
                usuario = User.query.filter_by(id=user_id).first()
                if usuario.saldo == None or usuario.saldo == 0:
                    return jsonify({'success': False, 'message': 'wallet = 0'})
                elif usuario.saldo < int(price):
                    return jsonify({'success': False, 'message': 'insufficiente amount of money'})
                else:
                    price = int(price)
                    comision = price * 0.05
                    usuario.saldo -= price

                    seller = User.query.filter_by(id=seller_uid).first()
                    seller.saldo += (price - comision)

                    filename_seller = f'{seller_uid}.txt'
                    filepath_seller = os.path.join(
                        f"{app.config['UPLOAD_FOLDER']}/{seller_uid}", filename_seller)

                    with open(filepath_seller, 'r') as file:
                        contenido = file.readlines()

                    contenido = [
                        linea for linea in contenido if linea.strip() != skin_uid]
                    file.close()

                    with open(filepath_seller, 'w') as file:
                        file.writelines(contenido)
                    file.close()

                    filename_user = f'{user_id}.txt'
                    filepath_user = os.path.join(
                        f"{app.config['UPLOAD_FOLDER']}/{user_id}", filename_user)

                    with open(filepath_user, 'a') as file:
                        file.write(str(skin_uid)+'\n')
                    file.close()

                    boleta = Transaccion(
                        price, comision, user_id, seller_uid, skin_uid)

                    skin = Skin.query.filter_by(id=skin_uid).first()
                    skin.user_id = usuario.id

                    posteo.ons_sale = False

                    db.session.add(boleta)
                    db.session.commit()
                    return jsonify({'success': True, 'boleta id': boleta.id})
        except Exception as e:
            return jsonify({'success': False, 'message': str(e)})
        finally:
            db.session.close()

    @app.route('/users/<user_id>/<user_saldo>', methods=['PATCH'])
    def update_user_saldo(user_id, user_saldo):
        returned_code = 200
        list_errors = []
        try:
            user = User.query.filter_by(id=user_id).first()

            user.saldo += int(user_saldo)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            returned_code = 500
            return jsonify({'success': False, 'message': str(e)})
        finally:
            db.session.close()
        if len(list_errors) > 0:
            returned_code = 400
            return jsonify({'success': False, 'message': 'Error updating employee', 'errors': list_errors}), returned_code
        elif returned_code != 200:
            abort(returned_code)
        else:
            return jsonify({"success": True, 'message': 'User is updated successfully!'}), returned_code

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            'success': False,
            'message': 'Method not allowed'
        }), 405

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'message': 'Resource not found'
        }), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            'success': False,
            'message': 'Internal Server error'
        }), 500

    return app
