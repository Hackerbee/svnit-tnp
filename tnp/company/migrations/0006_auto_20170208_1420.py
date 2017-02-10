# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 08:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_job_required_data_fields'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='perks',
        ),
        migrations.AddField(
            model_name='job',
            name='perks',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
    ]