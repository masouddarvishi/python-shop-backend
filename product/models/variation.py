from django.db import models
from user.models import Business
from .product import Product


class Variation(models.Model):
    pk = 'id'
    title = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    business = models.ForeignKey(Business, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'variations'
