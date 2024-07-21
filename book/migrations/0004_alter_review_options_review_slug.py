# Generated by Django 4.2.13 on 2024-07-21 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_remove_bibliography_review_bibliography_reader_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['created_on']},
        ),
        migrations.AddField(
            model_name='review',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
