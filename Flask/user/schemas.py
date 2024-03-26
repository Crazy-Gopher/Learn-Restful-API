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


from marshmallow import Schema, fields
class HealthStatusResp(Schema):
    Status = fields.Str()


def validate_str(val):
    if val == "":
        raise ValidationError("String can not be blank")

class RequestUser(Schema):
    id = fields.Int(description="Id of user", required=False, location='json')
    username = PinCode(validate=validate_str,description="username of a user", required=True, location='json')
    password = fields.Str(validate=validate.Length(min=1),description="password of a user",required=True, location='json')
    email = fields.Str(description="email of a user", required=True, location='json')
    is_active = fields.Bool(description="status of a user", required=True, location='json')

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
    id = fields.Int(description="Id of user", required=False, location='json')
    username = fields.Str(validate=validate_str,description="username of a user", required=True, location='json')
    password = fields.Str(validate=validate.Length(min=1),description="password of a user",required=True, location='json')
    email = fields.Str(description="email of a user", required=True, location='json')
    is_active = fields.Bool(description="status of a user", required=True, location='json')
    class Meta:
        strict = True

class UpdateRequestUser(Schema):
    username = fields.Str(validate=validate_str,description="username of a user", required=True, location='json')
    password = fields.Str(validate=validate.Length(min=1),description="password of a user",required=True, location='json')
    email = fields.Str(description="email of a user", required=True, location='json')
    is_active = fields.Bool(description="status of a user", required=True, location='json')
    class Meta:
        strict = True

class PatchRequestUser(Schema):
    username = fields.Str(validate=validate_str,description="username of a user", required=False, location='json')
    password = fields.Str(validate=validate.Length(min=1),description="password of a user",required=False, location='json')
    email = fields.Str(description="email of a user", required=False, location='json')
    is_active = fields.Bool(description="status of a user", required=False, location='json')
    class Meta:
        strict = True

class HealthStatusResp(Schema):
    service_status = fields.Str()