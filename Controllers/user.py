from flask import Flask
from flask_restplus import Resource ,Api,fields
from flask_restplus import reqparse

users = [{'name':'kirai'},]
app = Flask(__name__)
api = Api(app)
ns = api.namespace('user', description='user operations')
# todo = api.model('Todo', {
#     'email': fields.String(readonly=True, description='The email'),
#     'password': fields.String(required=True, description='The password')
# })
@api.route('/user')
class User (Resource):
    #region post解析器
    parser=reqparse.RequestParser()
    parser.add_argument('email',required=True,help='Email is required')
    parser.add_argument('password', required=True, help='Password is required')
    #endregion
    def get(self, name):
        find = [item for item in users if item['name'] == name]
        if len(find) == 0:
            return {
                'message': 'username not exist!'
            }, 403
        user = find[0]
        if not user:
            return {
                'message': 'username not exist!'
            }, 403
        return {
            'message': '',
            'user': user
        }
    @ns.param('email', 'The email')
    @ns.param('password', 'The password')
    def post(self, name):
        arg=self.parser.parse_args()
        user = {
            'name': name,
            'email': arg['email'],
            'password': arg['password']
        }
        users.append(user)
        return {
            'message': 'Insert user success',
            'user': user
        }
    def put(self, name):
        pass
    def delete(self, name):
        pass
@api.route('/users')   
class Users(Resource):
  def get(self):
      return {'users':users}
