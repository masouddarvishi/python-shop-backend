from rest_framework.authentication import BaseAuthentication, get_authorization_header
from django.contrib.auth import get_user_model

from rest_framework import exceptions
from django.utils.translation import ugettext_lazy as _

from user.respositories.userReposiory import UserRepository

from vendor.providers.base_provider import BaseProvider


class TokenAuthentication(BaseAuthentication, BaseProvider):
    keyword = 'Bearer'

    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        # validate keyword
        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None

        # get validated token
        token = self.validate_header(auth)

        # get user credential
        return self.authenticate_credentials(token)

    def authenticate_credentials(self, key):
        user = UserRepository().find_via_token(token=key)

        if user is None:
            raise exceptions.AuthenticationFailed(_('Invalid token.'))

        if not user.is_active:
            raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))

        return (user, user.api_token)

    def authenticate_header(self, request):
        return self.keyword
