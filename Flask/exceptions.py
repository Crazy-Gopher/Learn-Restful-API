from werkzeug import exceptions
from flask import Response, make_response, jsonify
from typing import Dict, List, Optional, Union, Any
from marshmallow.exceptions import ValidationError
from marshmallow import Schema, fields

class ErrorResp(Schema):
    message = fields.Str()
    error_code = fields.Str()
    error_details = fields.Mapping()

def _build_error_response(message: str, code: int,
                        details: Optional[Union[str, List, Dict]] = None) -> Response:
    resp: ErrorResp = ErrorResp()
    resp.message = message
    if details:
        resp.error_details = details
    return make_response(jsonify(resp.dump(resp)), code)

class SchemaValidationError(exceptions.UnprocessableEntity):
    description: str = "The request was well-formed but was unable to be followed due to semantic errors."

    def _init_(self, e: ValidationError, http_status_code,
                error_details: Optional[Dict[str, str]] = None):
        self.response: Response = _build_error_response(
            self.description, self.code, details=error_details)