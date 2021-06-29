from app import app
from ..views import users, helper, address

@app.route('/', methods=['GET'])
@helper.token_required
def root(current_user):
  return({ 'message': f'Hello {current_user.name}' })

@app.route('/users', methods=['POST'])
def post_user():
  return users.post_user()

@app.route('/users/<id>', methods=['PUT'])
@helper.token_required
def update_user(current_user, id):
  return users.update_user(current_user, id)

@app.route('/users', methods=['GET'])
@helper.token_required
def get_users(current_user):
  return users.get_users(current_user)

@app.route('/users/<id>', methods=['GET'])
@helper.token_required
def get_user(current_user, id):
  return users.get_user(current_user, id)

@app.route('/users/<id>', methods=['DELETE'])
@helper.token_required
def delete_user(current_user, id):
  return users.delete_user(current_user, id)

@app.route('/auth', methods=['POST'])
def authenticate():
  return helper.auth()

@app.route('/address', methods=['POST'])
@helper.token_required
def post_address(current_user):
  return address.post_address(current_user)

@app.route('/address', methods=['GET'])
@helper.token_required
def get_address(current_user):
  return address.get_user_address(current_user)