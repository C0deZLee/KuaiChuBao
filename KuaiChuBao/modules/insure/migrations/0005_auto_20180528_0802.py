# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-28 00:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insure', '0004_insureinfo_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insureinfo',
            name='jidongchecheshangrenyuanzerenbaoxian',
            field=models.CharField(default=0, max_length=100, verbose_name='\u673a\u52a8\u8f66\u8f66\u4e0a\u4eba\u5458\u8d23\u4efb\u4fdd\u9669'),
        ),
        migrations.AlterField(
            model_name='insureinfo',
            name='jidongchedisanzerenbaoxian',
            field=models.CharField(default=0, max_length=100, verbose_name='\u673a\u52a8\u8f66\u7b2c\u4e09\u8005\u8d23\u4efb\u4fdd\u9669'),
        ),
    ]