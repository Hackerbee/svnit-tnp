# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='bond_details',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
