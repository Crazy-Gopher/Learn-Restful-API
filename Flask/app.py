# from functools import wraps
from flask import Flask, Response, request, g, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from typing import Any, Callable, List, Type

from config import Config
from user.crud import UserView, UserDetailView, HealthCheckView

"""
#!/usr/bin/python3
# -- coding: utf-8 --
# from asr_python import load_profile_dotenv
# config path for all the files
# load_profile_dotenv(CONFIG_PATH)

# loading env variables before app start up
# env vars can be accessed from os.environ dict
"""

def register_paths(app: Flask):
    healthcheck_view: Callable[..., Response] = HealthCheckView.as_view(HealthCheckView.__name__)
    app.add_url_rule('/healthcheck',view_func=healthcheck_view)

    views = [
        (UserView, '/api/v1/users', ['GET', 'POST']),
        (UserDetailView, '/api/v1//users/<int:id>', ['GET', 'DELETE', 'PUT', 'PATCH'])
    ]

    for view_obj, view_path, methods in views:
        view = view_obj.as_view(view_obj.__name__)
        app.add_url_rule(view_path, view_func=view, methods=methods)




import time
import logging
from flask.json import JSONEncoder
from datetime import date

def run_before_request():
    g.start_time = time.time()

def run_after_request(response: Response):
    if response and response.status_code == 200:
        if request.url_rule:
            print(request.url_rule.rule)
        else:
            print(request.path)
        exec_start_time = g.start_time
        t = time.time() - exec_start_time
        print("time: " + str(t))
    return response

class CustomJSONEncoder(JSONEncoder):
    """
    This is a custom method to handle date object format in Flask JSONinfy.
    Default Date format: "Thu, 22 Oct 2020 00:00:00 GMT"
    New Date format: "2021-01-22"
    Any other type of data remains same, but can be edited here.
    """

    def default(self, o):  # pylint: disable=E0202
        if isinstance(o, date):
            return o.isoformat()
        return super().default(o)

def app_config(app: Flask) -> None:
    app.config.from_object(Config())
    app.before_request(run_before_request)
    app.after_request(run_after_request)
    app.logger.setLevel(logging.INFO)

def register_commands(app):
    from commands import add_admin
    app.cli.add_command(add_admin)

def create_app():
    # Initialize flask app with the name of the file
    app: Flask = Flask(__name__)
    app_config(app)
    register_paths(app)
    register_commands(app)
    app.SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/flask"
    # app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://user:password@host:port/database_name"
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/flask"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.json_encoder = CustomJSONEncoder
    db = SQLAlchemy(app)
    ma = Marshmallow(app)
    return app, db, ma

app, db, ma = create_app()

#this is our database model
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(200))
    email = db.Column(db.String(50), unique = True)
    is_active = db.Column(db.Boolean())

    def _init_(self, username, password, email, is_active):
        self.username = username
        self.password = password
        self.email = email
        self.is_active = is_active


# from app import ma
# from user.models import User
# class RequestUser(ma.Schema):
#     class Meta:
#         fields = ("username", "password", "email", "is_active")

# class ResponseUser(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = User
#         include_fk = True


with app.app_context():
    db.create_all()

@app.errorhandler(422)
@app.errorhandler(400)
def handle_validation_error(err):
    exc = getattr(err, "exc", None)
    if exc:
        headers = err.data["headers"]
        messages = exc.messages
    else:
        headers = None
        messages = ["Invalid request."]
    if headers:
        return {"errors": messages}, err.code, headers
    else:
        return {"errors": messages}, err.code


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8002", debug=True)



"""
# Path Paramter
@app.route('/user/<int:id>', methods=['GET'])
def show_user_profile(id):
    # show the user profile for that user
    return {"User": id}

# http://127.0.0.1:8001/search?name=John&location=Miami
@app.route('/search', methods=['GET'])
def search():
    args = request.args
    name = args.get('name')
    location = args.get('location')

    return {name:location}

import json
@app.route('/post_json', methods=['POST'])
def process_json():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = request.json
        # data = json.loads(request.data) # body - json data
        print(type(data))
        return data
        jsonn = request.get_json()
        print(type(jsonn))
        return jsonn
    else:
        return 'Content-Type not supported!'

@app.route('/post_form', methods=['POST'])
def process_form():
    data = request.form # form data
    print(data['username'])
    print(data['password'])
    return data

from flask import url_for
with app.test_request_context():
    print(url_for('index'))

def insd():
    return "Hello Kapil"

app.add_url_rule("/view_path", view_func=insd)
"""

# def admin_auth(api_method):
#     '''
#     Authentication method indended to decorate API calls which require
#     an admin user token for authentication
#     '''
#     @wraps(api_method)
#     def _admin_auth(**kwargs):
#         try:
#             api_method()
#         except Exception as e:
#             print(e.data)
#             print(e.code)
#             print(dir(e))
#             print(type(e))
#             return SchemaValidationError(e, 200, error_details={'username': ['String can not be blank']}).response
#     return _admin_auth
