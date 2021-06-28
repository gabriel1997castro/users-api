
from app.models.address import Address, address_schema
from app import db
from flask import request, jsonify


def post_address(current_user):
  
  country = request.json['country']
  state = request.json['state']
  city = request.json['city']
  postalCode = request.json['postalCode']
  number = request.json['number']
  complement = request.json['complement']
  users_id = current_user.id
  address = Address(country, state, city, postalCode, number, complement, users_id)

  try:
    db.session.add(address)
    db.session.commit()
    result = address_schema.dump(address)
    return jsonify({ 'message': 'successfully registered', 'data': result }), 201
  except Exception as e:
    print(e)
    return jsonify({ 'message': 'unable to create', 'data': {} }), 500