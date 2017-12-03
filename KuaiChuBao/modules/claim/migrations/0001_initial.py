# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-08 03:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate', models.CharField(max_length=200)),
                ('time', models.DateTimeField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='claims')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('claim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='claim.Claim')),
            ],
        ),
        migrations.CreateModel(
            name='InsuranceCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('national_id_number', models.CharField(max_length=200)),
                ('driver_license_number', models.CharField(max_length=200)),
                ('national_id_copy_top', models.ImageField(upload_to='users/national_id')),
                ('national_id_copy_down', models.ImageField(upload_to='users/national_id')),
                ('driver_license_copy_top', models.ImageField(upload_to='users/driver_license')),
                ('driver_license_copy_down', models.ImageField(upload_to='users/driver_license')),
            ],
        ),
        migrations.AddField(
            model_name='claim',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='claims', to='claim.InsuranceCompany'),
        ),
        migrations.AddField(
            model_name='claim',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='claims', to='claim.UserInfo'),
        ),
    ]
