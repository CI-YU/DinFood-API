from flask import Flask
from flask_restplus import Api

from Controllers.user import User

app=Flask(__name__)
api= Api(app)
api.add_resource(User, "/user/<string:name>")

if __name__ == "__main__":
    app.run()