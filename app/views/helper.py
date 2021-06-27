from config import SECRET_KEY
import datetime
from app import app
from werkzeug.security import check_password_hash
from flask import request, jsonify
from functools import wraps
from .users import user_by_username
import jwt

def auth():
  auth = request.authorization
  if not auth or not auth.username or not auth.password:
    return jsonify({ 'message': 'could not verify', 'WWW-Authenticate': 'Basic auth="Login required"' }), 401
  
  user = user_by_username(auth.username)
  if not user:
    return jsonify({ 'message': 'user not found', 'data': {}}), 401

  print(user)
  print(auth.password)
  print(user.password)

  if user and check_password_hash(user.password, auth.password):
    SECRET_KEY = app.config['SECRET_KEY']
    token = jwt.encode({ 'username': user.username, 'exp': datetime.datetime.now() + datetime.timedelta(hours=12) }, SECRET_KEY)
    return jsonify({'message': 'Validated successfully', 'token': token, 'exp': datetime.datetime.now() + datetime.timedelta(hours=12)})
  
  return jsonify({ 'message': 'could not verify', 'WWW-Authenticate': 'Basic auth="Login required"' }), 401