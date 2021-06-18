from rest_framework.authentication import BaseAuthentication, get_authorization_header
from rest_framework import exceptions
from django.utils.translation import ugettext_lazy as _


class TokenAuthentication(BaseAuthentication):
    keyword = 'Bearer'

    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None

        if len(auth) == 1:
            msg = _('Invalid token header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _('Invalid token header. Token string should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)

        raise exceptions.ValidationError('uchiha is near')
        pass

    def authenticate_header(self, request):
        return self.keyword
