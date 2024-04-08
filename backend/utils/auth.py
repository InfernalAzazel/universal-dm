from rest_framework.authentication import BaseAuthentication, get_authorization_header
from rest_framework.exceptions import AuthenticationFailed

from admin.models import User
from utils.helper import m_p
from utils.jwt import decode_access_token


class CustomTokenAuthentication(BaseAuthentication):

    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != b'bearer':
            return None

        if len(auth) == 1:
            raise AuthenticationFailed('Invalid token header. No credentials provided.')
        elif len(auth) > 2:
            raise AuthenticationFailed('Invalid token header. Token string should not contain spaces.')
        print(auth)
        try:
            token = auth[1]
            payload = decode_access_token(token)
        except Exception as e:  # Replace with your token error
            raise AuthenticationFailed('Invalid token.')
        user = m_p(User.objects()).first()
        # try:
        #     user = User.objects.get(username=payload['sub'])
        # except User.DoesNotExist:
        #     raise AuthenticationFailed('No user matching this token was found.')

        return user, token

    def authenticate_header(self, request):
        return 'Bearer'
