# Generated by Django 3.2.12 on 2022-02-23 16:20

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_likecount'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, db_index=True, max_length=255, verbose_name='image'),
        ),
    ]
