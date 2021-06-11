from core.models.user import User
from vendor.facades.repositories.baseRepository import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self):
        super(UserRepository, self).__init__(User)
