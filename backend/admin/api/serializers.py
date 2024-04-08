from admin.schema import InterfaceSchema, UserSchema
from utils.cmn_class import BaseSchemaSerializer


class InterfaceSerializer(BaseSchemaSerializer):
    schema_class = InterfaceSchema


class UserSerializer(BaseSchemaSerializer):
    schema_class = UserSchema
