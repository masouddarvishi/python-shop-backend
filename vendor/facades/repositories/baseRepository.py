from django.db import models


class BaseRepository:
    model = None

    def __init__(self, model):
        self.model = model

    def get_model(self) -> models:
        """ return instance of model"""
        return self.model

    def all(self):
        """ get all for resource """
        return self.model.objects.all()

    def find(self):
        pass

    def update(self):
        pass

    def update_object(self):
        pass