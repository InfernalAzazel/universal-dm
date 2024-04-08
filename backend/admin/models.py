import mongoengine

from utils.mixin import DBTimestampMixin


class User(DBTimestampMixin, mongoengine.Document):
    username = mongoengine.StringField()  # 帐号： quid1111
    password = mongoengine.StringField()  # 密码
    disabled = mongoengine.StringField()  # 禁用：True == 禁用
    role_names = mongoengine.StringField()  # 关联角色
    name = mongoengine.StringField()  # 姓名:  张三
    mail = mongoengine.StringField()  # 邮箱
    company = mongoengine.StringField()  # 公司
    department = mongoengine.StringField()  # 部门

    meta = {'collection': 'users'}


class Interface(DBTimestampMixin, mongoengine.Document):
    title = mongoengine.StringField()
    path = mongoengine.StringField()
    group = mongoengine.StringField()
    method = mongoengine.StringField()

    meta = {'collection': 'interface'}
