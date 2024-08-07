# Generated by Django 4.2.13 on 2024-08-07 09:07

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_bibliography_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='bibliography',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(blank=True, default='placeholder', max_length=255, null=True, verbose_name='image'),
        ),
    ]
