from flask import (Flask, request, jsonify, abort)
from .models import db, setup_db, Skin, User, Postventa, Transaccion
from flask_cors import CORS
from config.local import config
from .utilities import allowed_file
from datetime import datetime
from .users_controller import users_bp
from .authentication import authorize
from werkzeug.security import check_password_hash
import os
import openai

import jwt
import os
import sys


openai.api_key = "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"


def create_app(test_config=None):
    app = Flask(__name__)
    with app.app_context():
        app.config['UPLOAD_FOLDER'] = 'static/usuarios'
        app.register_blueprint(users_bp)
        setup_db(app, test_config['database_path'] if test_config else None)
        CORS(app, origins=['http://localhost:8080'])

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PATCH,POST,DELETE,OPTIONS')
        response.headers.add('Access-Control-Max-Age', '10')
        return response
    
    @app.route('/login', methods=['POST'])
    def login():
        body = request.json
        if 'nickname' not in body:
            return jsonify({'success': False, 'message': 'nickname is required'}), 400
        if 'e_mail' not in body:
            return jsonify({'success': False, 'message': 'email is required'}), 400
        if 'password' not in body:
            return jsonify({'success': False, 'message': 'password is required'}), 400

        nickname = body.get('nickname')
        email = body.get('e_mail')
        password = body.get('password')

        user = User.query.filter_by(nickname=nickname, e_mail=email).first()

        if not user:
            return jsonify({'success': False, 'message': 'user not found'}), 404

        if not user.verify_password(password):
            return jsonify({'success': False, 'message': 'invalid password'}), 401

        token = jwt.encode({
            'user_created_id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, config['SECRET_KEY'], config['ALGORITHM'])

        return jsonify({'success': True, 'token': token, 'user': user.serialize()}), 200


    @app.route('/process_message', methods=['POST'])
    def process_message():
        returned_code = 201
        list_errors = []
        try:
            # get the message and the champion name from the vue form
            data = request.json
            message = data.get('message')
            champion_name = data.get('champion_name')
            # create a prompt for GPT-3
            prompt = f"You'll be a league of legends expert. You'll be given a champion name from league of legends and a message, just do reply with the context of the message with an eloquent toneand in spanish. Here is your champion and message: {champion_name} and {message} , Now, reply with the context of the message: Well,  "
            # call the GPT-3 API with the prompt
            response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.2,
            max_tokens=400,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
            )
            response = response['choices'][0]['text']
        except Exception as e:
            print(e)
            print(sys.exc_info())
            returned_code = 500

        finally:
            if returned_code == 500:
                abort(returned_code)
            else:
                # return the response as a json object
                return jsonify({'response': response, 'prompt': message, 'success': True, 'message': 'message processed successfully!'}), returned_code

    
    
    @app.route('/skins', methods=['POST'])
    @authorize
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
                skin.image = os.path.join("static/campeones",f'{champion_name}',f'{name}.jpg')  
                db.session.commit()
                db.session.close()
                skin = db.session.merge(skin)
                skin.serialize()
                

        except Exception as e:
            print(e)
            print(sys.exc_info())
            db.session.rollback()
            returned_code = 500

        finally:
            db.session.close()

        if returned_code == 400:
            return jsonify({'success': False, 'message': "Error creating skin", 'errors': list_errors}), returned_code
        elif returned_code != 201:
            abort(returned_code)
        else:
            return jsonify({'success': True, 'message': "skin created successfully!", 'skin': skin.serialize()}), returned_code

    @app.route('/skins/<user_id>', methods=['GET'])
    @authorize
    def user_skins(user_id):
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
        
    @app.route('/posts', methods=['GET'])
    def postsventa():
        try:
            posts = Postventa.query.all()
            posts_serialized = [post.serialize() for post in posts]
            return jsonify({'success': True, 'serialized': posts_serialized})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})

    @app.route('/skins', methods=['GET'])
    def get_all_db_skins():
        try:
            skins = Skin.query.all()
            skins_serialized = [skin.serialize() for skin in skins]
            return jsonify({'success': True, 'skins': skins_serialized})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})

    @app.route('/posts/<user_id>', methods=['POST'])
    @authorize
    def create_postventa(user_id):
        returned_code = 201
        list_errors = []
        try:

            user = User.query.filter(User.id == user_id).first()
            if not user:
                returned_code = 404
            else:

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
                    skin_image = os.path.join(
                        "static/campeones", f'{champion}', f'{name}.jpg')
                    on_sale = True
                    skin = Skin.query.get(skin_id)
                    if not skin:
                        returned_code = 404
                    else:
                        postventa = Postventa(title, user_id, skin_id, on_sale, int(
                            price), champion, skin_image, name)
                        db.session.add(postventa)
                        db.session.commit()
                        db.session.close()  # cerramos la sesión después del commit
                        # reasociamos la instancia a una nueva sesión
                        postventa = db.session.merge(postventa)
                        postventa.serialize()  # llamamos al método serialize sin error

        except Exception as e:
            print(sys.exc_info())
            db.session.rollback()
            returned_code = 500

        finally:
            db.session.close()

        if returned_code == 400:
            return jsonify({'success': False, 'message': 'Error creating Post', 'errors': list_errors}), returned_code
        elif returned_code != 201:
            abort(returned_code)
        else:
            return jsonify({'success': True, 'message': 'Post created successfully!', 'post': postventa.serialize()}), returned_code

    @app.route('/users/<user_id>/skins', methods=['POST'])
    @authorize
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

                    posteo.on_sale = False

                    db.session.add(boleta)
                    db.session.commit()

        except Exception as e:
            print(e)
            print(sys.exc_info())
            db.session.rollback()
            returned_code = 500
        finally:
            db.session.close()

        if returned_code == 400:
            return jsonify({'success': False, 'message': 'Error buying skin', 'errors': list_errors}), returned_code
        elif returned_code != 201:
            abort(returned_code)
        else:
            return jsonify({'success': True, 'message': 'Skin sold successfully!'}), returned_code

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
