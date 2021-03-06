# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 19:39
from __future__ import unicode_literals

import apps.beer.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='image',
            field=models.ImageField(blank=True, max_length=400, null=True, upload_to=apps.beer.models.beer_image_upload_location, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='beer',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
    ]
