from flask import Flask
from flask_restplus import Api ,Resource

#from Controllers.user import User ,Users
from Controllers import api

# app=Flask(__name__)
# api= Api(app)
# api.add_resource(User, "/user/<string:name>")
# api.add_resource(Users, "/users")
# @api.route('/hello')
# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}

app = Flask(__name__)
api.init_app(app)

if __name__ == '__main__':
    app.run()