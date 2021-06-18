from core.models.user import User
from vendor.repositories.baseRepository import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self):
        super(UserRepository, self).__init__(User)

    def find_via_token(self, token):
        return self.find(api_token=token)

    def find_via_email(self, email):
        return self.find(email=email)
