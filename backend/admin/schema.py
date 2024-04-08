from marshmallow_mongoengine import ModelSchema
from admin.models import Interface, User


class InterfaceSchema(ModelSchema):
    class Meta:
        model = Interface


class UserSchema(ModelSchema):
    class Meta:
        model = User
