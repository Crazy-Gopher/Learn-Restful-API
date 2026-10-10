import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from config import Config
from middlewares import run_before_request, run_after_request


def app_config(app: Flask) -> None:
    app.config.from_object(Config())
    app.before_request(run_before_request)
    app.after_request(run_after_request)
    app.logger.setLevel(logging.INFO)


def create_app():
    app: Flask = Flask(__name__)
    app_config(app)
    db = SQLAlchemy(app)
    ma = Marshmallow(app)
    return app, db, ma


app, db, ma = create_app()

# Models must be imported before create_all() so tables are registered
from user.models import User  # noqa: F401

with app.app_context():
    db.create_all()

# Import and register routes
import routes





# from app import ma
# from user.models import User
# class RequestUser(ma.Schema):
#     class Meta:
#         fields = ("username", "password", "email", "is_active")

# class ResponseUser(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = User
#         include_fk = True


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

# from flask.json import JSONEncoder
#!/usr/bin/python3
# -- coding: utf-8 --
# from asr_python import load_profile_dotenv
# config path for all the files
# load_profile_dotenv(CONFIG_PATH)

# loading env variables before app start up
# env vars can be accessed from os.environ dict


# class CustomJSONEncoder(JSONEncoder):
#
#     """
#     # app.json_encoder = CustomJSONEncoder
#     This is a custom method to handle date object format in Flask JSONinfy.
#     Default Date format: "Thu, 22 Oct 2020 00:00:00 GMT"
#     New Date format: "2021-01-22"
#     Any other type of data remains same, but can be edited here.
#     """

#     def default(self, o):  # pylint: disable=E0202
#         if isinstance(o, date):
#             return o.isoformat()
#         return super().default(o)
