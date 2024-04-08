from datetime import timedelta
from rest_framework import status, serializers, views
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from admin.models import User
from backend.settings import JWT_MINUTES
from utils.helper import m_p
from utils.jwt import create_access_token


class LoginView(views.APIView):
    permission_classes = [AllowAny]

    class RequestSerializer(serializers.Serializer):
        username = serializers.CharField(required=True, max_length=150)
        password = serializers.CharField(required=True, max_length=150)

        def validate(self, attrs):
            self.username = attrs.get('username')
            self.password = attrs.get('password')
            # 查询用户是否存在
            user = m_p(User.objects(username=self.username, password=self.password)).first()
            if user is None:
                raise serializers.ValidationError("Invalid credentials")
            return attrs

    def post(self, request: Request):
        serializer = self.RequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        access_token = create_access_token(
            data={'sub': serializer.username},
            expires_delta=timedelta(minutes=JWT_MINUTES)
        )
        response = {'access_token': access_token, 'token_type': 'bearer'}
        return Response(response, status=status.HTTP_200_OK)
