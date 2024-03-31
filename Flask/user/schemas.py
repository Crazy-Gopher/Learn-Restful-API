from marshmallow import Schema, validate, post_load, EXCLUDE, fields
from webargs import ValidationError
from datetime import datetime

from marshmallow import fields, ValidationError


class PinCode(fields.Field):
    """Field that serializes to a string of numbers and deserializes
    to a list of numbers.
    """

    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return ""
        return value.upper()

    def _deserialize(self, value, attr, data, **kwargs):
        try:
            return value.lower()
        except ValueError as error:
            raise ValidationError("Pin codes must contain only digits.") from error



class HealthStatusResp(Schema):
    Status = fields.Str()


def validate_str(val):
    if val == "":
        raise ValidationError("String can not be blank")

class RequestUser(Schema):
    id = fields.Int(required=False, metadata= {'description': 'Id of user', 'location': 'json'})
    username = fields.Str(validate=validate_str, required=True, metadata= {'description': 'username of a user', 'location': 'json'})
    password = fields.Str(validate=validate.Length(min=1), required=True, metadata= {'description': 'password of a user', 'location': 'json'})
    email = fields.Str(required=True, metadata= {'description': 'email of a user', 'location': 'json'})
    is_active = fields.Bool(required=True, metadata= {'description': 'status of a user', 'location': 'json'})
    class Meta:
        strict = True
    # callback_config = fields.Nested(
    #     CallbackRequest._name_, many=False,
    #     description="Callback configuration for the application",
    #     required=False,
    #     location='json',
    #     attribute=User.cb_config.attr_name
    # )

    # @post_load
    # def make_app_client(self, data, **kwargs):
    #     return User(**data)

    class Meta:
        strict = True



class ResponseUser(Schema):
    id = fields.Int(required=False, metadata= {'description': 'Id of user', 'location': 'json'})
    username = fields.Str(validate=validate_str, required=True, metadata= {'description': 'username of a user', 'location': 'json'})
    password = fields.Str(validate=validate.Length(min=1), required=True, metadata= {'description': 'password of a user', 'location': 'json'})
    email = fields.Str(required=True, metadata= {'description': 'email of a user', 'location': 'json'})
    is_active = fields.Bool(required=True, metadata= {'description': 'status of a user', 'location': 'json'})
    class Meta:
        strict = True

class UpdateRequestUser(Schema):
    username = fields.Str(validate=validate_str, required=True, metadata= {'description': 'username of a user', 'location': 'json'})
    password = fields.Str(validate=validate.Length(min=1), required=True, metadata= {'description': 'password of a user', 'location': 'json'})
    email = fields.Str(required=True, metadata= {'description': 'email of a user', 'location': 'json'})
    is_active = fields.Bool(required=True, metadata= {'description': 'status of a user', 'location': 'json'})
    class Meta:
        strict = True

class PatchRequestUser(Schema):
    username = fields.Str(validate=validate_str, required=False, metadata= {'description': 'username of a user', 'location': 'json'})
    password = fields.Str(validate=validate.Length(min=1), required=False, metadata= {'description': 'password of a user', 'location': 'json'})
    email = fields.Str(required=False, metadata= {'description': 'email of a user', 'location': 'json'})
    is_active = fields.Bool(required=False, metadata= {'description': 'status of a user', 'location': 'json'})
    class Meta:
        strict = True


class HealthStatusResp(Schema):
    service_status = fields.Str()
