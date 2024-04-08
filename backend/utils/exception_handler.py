from rest_framework import serializers
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # 首先调用 REST 框架的默认异常处理程序,
    # 获取标准错误响应.
    response = exception_handler(exc, context)
    # 定义响应数据
    data = {
        'status_code': response.status_code,
        'success': False,
    }
    # 根据异常类型提取错误信息
    if isinstance(exc, serializers.ValidationError):
        # 对 ValidationError进行处理
        error_messages = []
        for field, errors in exc.detail.items():
            for error in errors:
                error_message = f"{field}: {str(error)}"
                print(error_message)
                error_messages.append(error_message)

        detail_message = "\n".join(error_messages)
        data['detail'] = detail_message
    else:
        data['detail'] = str(exc)

    response.data = data
    return response
