# Generated by Django 4.2.13 on 2024-08-08 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_bibliography_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='bibliography',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
