# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 14:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0003_bikes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bikes',
            old_name='category',
            new_name='ridecategory',
        ),
    ]
