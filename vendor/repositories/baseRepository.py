from django.db import models
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


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

    def find(self, **condition):
        try:
            return self.model.objects.get(**condition)
        except ObjectDoesNotExist or MultipleObjectsReturned:
            return None

    def update(self):
        pass

    def update_object(self, instance, **data):
        for key in data.keys():
            setattr(instance, key, data[key])
        instance.save()

        return instance
