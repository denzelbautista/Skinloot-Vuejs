from flask_sqlalchemy import SQLAlchemy
from config.local import config
import uuid
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import sys

db = SQLAlchemy()

def setup_db(app, database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = config['DATABASE_URI'] if database_path is None else database_path
    app.debug=True
    #db.app = app
    db.init_app(app)
    db.create_all()

class Skin(db.Model):
    __tablename__ = 'skins'
    id = db.Column(db.String(36),primary_key=True,unique=True,default=lambda: str(uuid.uuid4()), server_default=db.text("uuid_generate_v4()"))
    name = db.Column(db.String(100),unique=False,nullable=False)
    champion_name = db.Column(db.String(100),unique=False,nullable=False)
    rarity = db.Column(db.String(100),unique=False,nullable=False)
    image = db.Column(db.String(500),nullable=True)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('skins', post_update=True))

    def __init__(self,name,champion_name,rarity,user_id):
        self.name = name
        self.champion_name = champion_name
        self.rarity = rarity
        self.user_id = user_id
    
    def serialize(self):
        return{
            'id': self.id,
            'name' : self.name,
            'champion_name': self.champion_name,
            'rarity' : self.rarity,
            'image' : self.image,
            'user_id' : self.user_id
        }

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(36),primary_key=True,default=lambda: str(uuid.uuid4()), server_default=db.text("uuid_generate_v4()"))
    nickname = db.Column(db.String(100),unique=False,nullable=False)
    skins_hashes = db.Column(db.String(100),unique=False,nullable=True)
    e_mail = db.Column(db.String(100),unique=True,nullable=False)
    password_hash = db.Column(db.String(400),unique=False,nullable=False)
    saldo = db.Column(db.Integer,nullable=True,server_default='0')
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.text("now()"))
    image = db.Column(db.String(500),nullable=True)

    @property
    def password(self):
        raise AttributeError('Password is not readable')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __init__(self,nickname,e_mail,password):
        self.nickname = nickname
        self.e_mail = e_mail    
        self.password = password
        self.created_at = datetime.utcnow()

    
    def get_id(self):
        return self.id

    def serialize(self):
        return{
            'id': self.id,
            'nickname' : self.nickname,
            'e_mail' : self.e_mail,
            'saldo' : self.saldo
        }
    
    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            user_created_id = self.id
        except Exception as e:
            print(sys.exc_info())
            print('e: ', e)
            db.session.rollback()
        finally:
            db.session.close()
        
        return user_created_id

class Postventa(db.Model):
    __tablename__ = 'postventa'
    id = db.Column(db.String(36),primary_key=True,default=lambda: str(uuid.uuid4()), server_default=db.text("uuid_generate_v4()"))
    title = db.Column(db.String(100),unique=False,nullable=False)
    campeon = db.Column (db.String(100), nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    skin_id = db.Column (db.String(36), db.ForeignKey('skins.id'), nullable=False)
    skin_image = db.Column(db.String(500),nullable=True)
    nombre = db.Column (db.String(100), nullable=False)
    on_sale = db.Column(db.Boolean,unique=False,nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.text("now()"))
    skin = db.relationship('Skin', backref=db.backref('postventa', post_update=True))
    user = db.relationship('User', backref=db.backref('postventa', post_update=True))

    def __init__(self,title,user_id,skin_id,on_sale,precio,campeon, skin_image,nombre):
        self.title = title
        self.user_id = user_id
        self.skin_id = skin_id
        self.on_sale = on_sale
        self.precio = precio
        self.campeon = campeon
        self.skin_image = skin_image
        self.nombre = nombre

    def serialize(self):
        return{
            'id': self.id,
            'title' : self.title,
            'user_id' : self.user_id,
            'skin_id': self.skin_id,
            'on_sale' : self.on_sale,
            'skin_image' : self.skin_image,
            'precio' : self.precio,
            'nombre' : self.nombre,
            'campeon': self.campeon
        }

class Transaccion(db.Model):
    __tablename__ = 'transacciones'
    id = db.Column(db.String(36), primary_key=True, unique=True, default=lambda: str(uuid.uuid4()), server_default=db.text("uuid_generate_v4()"))
    fecha = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.text("now()"))
    precio = db.Column(db.Float, nullable=False)
    comision = db.Column(db.Float, nullable=False)
    id_comprador = db.Column(db.String(36), nullable=False)
    id_vendedor = db.Column(db.String(100), nullable=False)
    id_skin = db.Column(db.String(100), nullable=False)

    def __init__(self,precio, comision, id_comprador, id_vendedor, id_skin):
        self.precio = precio
        self.comision = comision
        self.id_comprador = id_comprador
        self.id_vendedor = id_vendedor
        self.id_skin = id_skin

    def serialize(self):
        return {
            'id': self.id,
            'fecha': self.fecha,
            'precio': self.precio,
            'comision': self.comision,
            'id_comprador': self.id_comprador,
            'id_vendedor': self.id_vendedor,
            'id_skin': self.id_skin,
        }
    
class Trade(db.Model):
    __tablename__ = 'trades'
    id = db.Column(db.String(36), primary_key=True, unique=True, default=lambda: str(uuid.uuid4()), server_default=db.text("uuid_generate_v4()"))
    fecha_inicio = db.Column(db.DateTime, nullable=False)
    nombre_comprador = db.Column(db.String(100), nullable=False)
    nombre_skin_comprador = db.Column(db.String(100), nullable=False)
    nombre_vendedor = db.Column(db.String(100), nullable=False)
    nombre_skin_vendedor = db.Column(db.String(100), nullable=False)

    def __init__(self, fecha_inicio, nombre_comprador, nombre_skin_comprador, nombre_vendedor, nombre_skin_vendedor):
        self.fecha_inicio = fecha_inicio
        self.nombre_comprador = nombre_comprador
        self.nombre_skin_comprador = nombre_skin_comprador
        self.nombre_vendedor = nombre_vendedor
        self.nombre_skin_vendedor = nombre_skin_vendedor

    def serialize(self):
        return {
            'id': self.id,
            'fecha_inicio': self.fecha_inicio,
            'nombre_comprador': self.nombre_comprador,
            'nombre_skin_comprador': self.nombre_skin_comprador,
            'nombre_vendedor': self.nombre_vendedor,
            'nombre_skin_vendedor': self.nombre_skin_vendedor
        }
    
