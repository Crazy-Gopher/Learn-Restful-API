# from click import decorators
from typing import Dict
from flask.views import MethodView
from webargs.flaskparser import use_args, use_kwargs
from user.schemas import RequestUser, ResponseUser, UpdateRequestUser, PatchRequestUser, HealthStatusResp
from http import HTTPStatus


from flask import request, jsonify, Response, helpers, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import json

users_schema = ResponseUser(many=True)
user_schema = ResponseUser()



class HealthCheckView(MethodView):
    """ APIs to query status of the services """
    # methods = ['GET']
    # decorators = [admin_auth]

    def get(self) -> Response:
        service_status_resp = dict(Status="Up")
        resp = Response(json.dumps(service_status_resp), status=HTTPStatus.OK, mimetype='application/json')
        # result = HealthStatusResp().dump(service_status_resp)
        # resp: Response = helpers.bnm(jsonify(result), HTTPStatus.OK)
        return resp

from sqlalchemy.orm.exc import NoResultFound
class UserView(MethodView):
    
    def get(self) -> Response:
        from app import db, User
        users = User.query.all()
        result = users_schema.dump(users)
        return jsonify(result)

    # @use_args(RequestUser(), locations='header')
    # @use_args(RequestUser(), locations=('json'))
    # @use_kwargs(RequestUser, locations='path')
    # @use_kwargs(RequestUser(), locations=('view_args'))
    # @use_kwargs(RequestUser(), locations='query')
    # @use_kwargs(RequestUser(), locations=('querystring'))
    @use_args(RequestUser(), location='json')
    def post(self, request: RequestUser):
        from app import db, User
        email = request.get("email")
        try:
            user = db.session.execute(db.select(User).filter_by(email=email)).one()
        except NoResultFound:
            user = None
        if user:
            resp: Response = make_response({"Error": f"User already exist with email {email}"}, HTTPStatus.BAD_REQUEST)
            return resp
        user = User(username = request.get("username"),
            password = request.get("password"),
            email = request.get("email"),
            is_active = request.get("is_active"))
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user)
        # return jsonify(result)
        # resp: Response = helpers.make_response(result, HTTPStatus.CREATED)
        resp: Response = make_response(result, HTTPStatus.CREATED)
        return resp


class UserDetailView(MethodView):

    def get(self, id: int):
        from app import db, User
        user = User.query.get(id)
        result = user_schema.dump(user)
        return jsonify(result)
        resp = ResponseUser()
        resp.username = user.username
        resp.password = user.password
        resp.email = user.email
        resp.id = user.id
        resp.is_active = user.is_active
        # response: Response = helpers.make_response(jsonify({"status":"on"}), HTTPStatus.OK)
        response: Response = helpers.make_response(jsonify(resp.dump(resp)), HTTPStatus.OK)
        response.headers["Content-Type"] = "application/json"
        return response
        # TypeError: The view function did not return a valid response. The return type must be a string, dict, 
        # list, tuple with headers or status, Response instance, or WSGI callable, but it was a int.

    def delete(self, id: int):
        from app import db, User
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify(result)

    @use_args(UpdateRequestUser(), location='json')
    def put(self, request: Dict, id:int):
        from app import db, User
        user = User.query.get(id)
        # user.update(**request)
        user.username = request.get("username")
        user.password = request.get("password")
        user.email = request.get("email")
        user.is_active = request.get("is_active")
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify(result)

    @use_args(PatchRequestUser(), location='json')
    def patch(self, request: Dict, id:int):
        from app import db, User
        user = User.query.get(id)
        if request:
            if request.get("username"):
                user.username = request.get("username")
            if request.get("password"):
                user.password = request.get("password")
            if request.get("email"):
                user.email = request.get("email")
            if request.get("is_active"):
                user.is_active = request.get("is_active")
            db.session.commit()
        result = user_schema.dump(user)
        return jsonify(result)