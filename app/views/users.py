from werkzeug.security import generate_password_hash
from app import db
from flask import request, jsonify
from ..models.user import User, user_schema, users_schema

def post_user():
  username = request.json['username']
  password = request.json['password']
  name = request.json['name']
  email = request.json['email']
  cpf = request.json['cpf']
  pis = request.json['pis']
  pass_hash = generate_password_hash(password)
  user = User(username, pass_hash, name, email, cpf, pis)
  try:
    db.session.add(user)
    db.session.commit()
    result = user_schema.dump(user)
    return jsonify({ 'message': 'successfully registered', 'data': result }), 201
  except Exception as e:
    print(e)
    return jsonify({ 'message': 'unable to create', 'data': {} }), 500

def update_user(id):
  username = request.json['username']
  password = request.json['password']
  name = request.json['name']
  email = request.json['email']
  cpf = request.json['cpf']
  pis = request.json['pis']
  
  user = User.query.get(id)

  if not user:
    return jsonify({ 'message': "User don't exit", 'data': {} }), 404

  pass_hash = generate_password_hash(password)

  try:
    user.username = username
    user.password = pass_hash
    user.name = name
    user.email = email
    user.cpf = cpf
    user.pis = pis
  
    db.session.commit()
    result = user_schema.dump(user)
    print(result)
    return jsonify({ 'message': 'successfully registered', 'data': result }), 201
  except Exception as e:
    print('ERRO in UPDATE:', e)
    return jsonify({ 'message': 'unable to create', 'data': {} }), 500