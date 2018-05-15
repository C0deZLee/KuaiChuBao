# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-15 06:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insure', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='insureinfo',
            name='step',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='insureinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='insures', to='user.User'),
        ),
    ]
