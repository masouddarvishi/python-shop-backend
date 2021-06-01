# Generated by Django 3.2 on 2021-04-30 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='variation',
            name='business',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.business'),
        ),
        migrations.AddField(
            model_name='variation',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.product'),
        ),
    ]
