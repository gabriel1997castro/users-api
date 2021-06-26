from app import app
from ..views import users

@app.route('/', methods=['GET'])
def root():
  return({ 'message': 'Hello world!' })

@app.route('/users', methods=['POST'])
def post_user():
  return users.post_user()

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
  return users.update_user(id)

@app.route('/users', methods=['GET'])
def get_users():
  return users.get_users()

@app.route('/users/<id>', methods=['GET'])
def get_user(id):
  return users.get_user(id)