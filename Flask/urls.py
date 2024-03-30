
from typing import Any, Callable, List, Type
from flask import Flask, Response, request, g, current_app
from user.crud import UserView, UserDetailView, HealthCheckView

def register_paths(app: Flask):
    healthcheck_view: Callable[..., Response] = HealthCheckView.as_view(HealthCheckView.__name__)
    app.add_url_rule('/healthcheck',view_func=healthcheck_view)

    views = [
        (UserView, '/api/v1/users/', ['GET', 'POST']),
        (UserDetailView, '/api/v1//users/<int:id>/', ['GET', 'DELETE', 'PUT', 'PATCH'])
    ]

    for view_obj, view_path, methods in views:
        view = view_obj.as_view(view_obj.__name__)
        app.add_url_rule(view_path, view_func=view, methods=methods)
