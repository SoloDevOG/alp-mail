# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-11 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
