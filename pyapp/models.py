from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from pyapp import db, loginManager
from datetime import datetime
from flask_login import UserMixin


@loginManager.user_loader
def loadUser(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    address = db.Column(db.String(256), nullable=False)
    phone = db.Column(db.String(16), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    image_file = db.Column(db.String(32), nullable=False,
                           default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def get_reset_token(self, expires=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        # Function to determine how the 'User' will look when printed out
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class StoreItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    price = db.Column(db.DECIMAL, nullable=False)
    image = db.Column(db.String(32), nullable=False, default='default_item.jpg')
    sale = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        # Function to determine how the 'StoreItem' will look when printed out
        return f"StoreItem('{self.name}', '{self.price}', '{self.image}')"


