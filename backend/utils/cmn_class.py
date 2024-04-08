# 封装各个公用用途的类

from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination


# 自定义 Mongodb 序列化
class BaseSchemaSerializer(serializers.Serializer):
    schema_class = None  # 定义一个占位的 schema 类属性

    def get_schema(self):
        # 确保每个子类都设置了schema_class
        if self.schema_class is None:
            raise serializers.ValidationError("must be set schema_class")
        return self.schema_class()

    def to_representation(self, instance):
        schema = self.get_schema()
        return schema.dump(instance)

    def to_internal_value(self, data):
        schema = self.get_schema()
        return schema.load(data).data


# 自定义分页器
class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10  # 自定义每页显示的数量
    max_page_size = 100  # 最大允许每页显示的数量
    # 别名
    page_query_param = 'current_page'  # 当前页面数量的别名
    page_size_query_param = 'page_size'  # 指定每页数量的别名
    max_page_size_query_param = 'page_max_size'  # 每页最大数量的别名
