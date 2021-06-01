from django.db import models
from .user import User


class Business(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(max_length=500, blank=True)
    logo = models.ImageField(null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    users = models.ManyToManyField(User, related_name='business_user')

    class Meta:
        db_table = 'businesses'
