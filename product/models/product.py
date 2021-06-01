from django.db import models


class Product(models.Model):
    pk = 'id'
    slug = models.SlugField(max_length=255, unique=True)
    title = models.SlugField(max_length=255)
    description = models.TextField(max_length=500, blank=True)
    thumbnail = models.ImageField(null=True, upload_to='get_image_file_path')

    class Meta:
        db_table = 'products'
