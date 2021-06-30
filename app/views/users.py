from app.utils.functions import validate_cpf, validate_email
from werkzeug.security import generate_password_hash
from app import db
from flask import request, jsonify
from ..models.users import Users, user_schema, users_schema
from ..models.address import address_schema


def post_user():
    password = request.json['password']
    name = request.json['name']
    email = request.json['email']
    cpf = request.json['cpf']
    pis = request.json['pis']
    pass_hash = generate_password_hash(password)
    user = Users(pass_hash, name, email, cpf, pis)

    try:
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({'message': 'successfully registered', 'data': result}), 201
    except Exception as e:
        print(e)
        return jsonify({'message': 'unable to create', 'data': {}}), 500


def update_user(current_user, id):
    password = request.json['password']
    name = request.json['name']
    email = request.json['email']
    cpf = request.json['cpf']
    pis = request.json['pis']

    user = Users.query.get(id)

    if not user:
        return jsonify({'message': "User don't exit", 'data': {}}), 404

    pass_hash = generate_password_hash(password)

    try:
        user.password = pass_hash
        user.name = name
        user.email = email
        user.cpf = cpf
        user.pis = pis

        db.session.commit()
        result = user_schema.dump(user)
        print(result)
        return jsonify({'message': 'successfully registered', 'data': result}), 201
    except Exception as e:
        print('ERRO in UPDATE:', e)
        return jsonify({'message': 'unable to create', 'data': {}}), 500


def get_users(current_user):
    users = Users.query.all()

    if users:
        result = users_schema.dump(users)
        return jsonify({'message': 'successfully fetched', 'data': result})

    return jsonify({'message': 'nothing found', 'data': {}})


def get_user(current_user, id):
    user = Users.query.get(id)
    if user:
        result = user_schema.dump(user)
        return jsonify({'message': 'successfully fetched', 'data': result}), 201
    return jsonify({'message': 'user not found', 'data': {}}), 404


def delete_user(current_user, id):
    user = Users.query.get(id)
    if not user:
        return jsonify({'message': 'user not found', 'data': {}}), 404

    if user:
        try:
            db.session.delete(user)
            db.session.commit()
            result = user_schema.dump(user)
            return jsonify({'message': 'successfully deleted', 'data': result}), 200
        except:
            return jsonify({'message': 'unable to delete user', 'data': {}}), 500


def user_by_username(username):
    username_type = ''
    if validate_email(username):
        username_type = 'email'
    elif validate_cpf(username):
        username_type = 'cpf'
    else:
        username_type = 'pis'
    print('username', username_type)
    print('username', Users.query.filter(getattr(Users, username_type) == username).one())
    try:
        return Users.query.filter(getattr(Users, username_type) == username).one()
    except:
        return None
