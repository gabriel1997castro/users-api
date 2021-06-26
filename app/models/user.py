import datetime
from app import db, ma

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  password = db.Column(db.String(200), nullable=False)
  name = db.Column(db.String(60), nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  cpf = db.Column(db.String(11), nullable=False)
  pis = db.Column(db.String(11), nullable=False)
  address = db.relationship('Address', backref='user', lazy=True, uselist=False)
  created_on = db.Column(db.DateTime, default=datetime.datetime.now())

  def __init__(self, username, password, name, email, cpf, pis):
    self.username = username
    self.password = password
    self.name = name
    self.email = email
    self.cpf = cpf
    self.pis = pis

"""Schema do Marshmallow para facilitar o uso de JSON"""
class UserSchema(ma.Schema):
  class Meta:
    fields = ('id', 'username', 'name', 'email', 'cpf', 'pis', 'created_on')
