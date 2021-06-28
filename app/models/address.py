from app import db, ma

class Address(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  country = db.Column(db.String(50), nullable=False)
  state = db.Column(db.String(50), nullable=False)
  city = db.Column(db.String(50), nullable=False)
  postalCode = db.Column(db.String(10), nullable=False)
  number = db.Column(db.String(20), nullable=False)
  complement = db.Column(db.String(50), nullable=False)
  users_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

  def __init__(self, country, state, city, postalCode, number, complement, users_id):
    self.country = country
    self.state = state
    self.city = city
    self.postalCode = postalCode
    self.number = number
    self.complement = complement
    self.users_id = users_id

class AddressSchema(ma.Schema):
  class Meta:
    fields = ('id', 'country', 'state', 'city', 'postalCode', 'number', 'complement', 'user_id')

address_schema = AddressSchema()
addresses_schema = AddressSchema(many=True)