from config import SECRET_KEY
import datetime
from app import app
from werkzeug.security import check_password_hash
from flask import request, jsonify
from functools import wraps
from .users import user_by_username
import jwt


def token_required(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    auth_header = request.headers.get('Authorization')
    token = None
    if auth_header:
      token = auth_header.split(" ")[1]
    if not token:
      return jsonify({ 'message': 'token is missing', 'data': {} }), 401
    try:
      data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
      current_user = user_by_username(username=data['username'])
    except:
      return jsonify({ 'message': 'token is invalid or expired', 'data': {} }), 401
    return f(current_user, *args, **kwargs)
  return decorated


def auth():
  auth = request.authorization
  if not auth or not auth.username or not auth.password:
    return jsonify({ 'message': 'could not verify', 'WWW-Authenticate': 'Basic auth="Login required"' }), 401
  
  user = user_by_username(auth.username)
  if not user:
    return jsonify({ 'message': 'user not found', 'data': {}}), 401

  if user and check_password_hash(user.password, auth.password):
    SECRET_KEY = app.config['SECRET_KEY']
    token = jwt.encode({ 'username': user.email, 'exp': datetime.datetime.now() + datetime.timedelta(hours=12) }, SECRET_KEY, algorithm="HS256")
    return jsonify({'message': 'Validated successfully', 'token': token, 'exp': datetime.datetime.now() + datetime.timedelta(hours=12)})
  
  return jsonify({ 'message': 'could not verify', 'WWW-Authenticate': 'Basic auth="Login required"' }), 401
