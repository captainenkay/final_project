# Generated by Django 2.2 on 2019-07-24 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='category',
            new_name='product',
        ),
    ]
