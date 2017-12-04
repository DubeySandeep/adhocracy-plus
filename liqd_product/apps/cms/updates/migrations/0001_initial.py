# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KeepMeUpdatedEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interested_as_municipality', models.BooleanField()),
                ('interested_as_citizen', models.BooleanField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
