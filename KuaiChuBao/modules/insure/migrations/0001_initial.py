# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-24 04:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InsuranceCompanyForInsure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('url', models.CharField(blank=True, max_length=200, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='companies_logo/')),
            ],
        ),
        migrations.CreateModel(
            name='InsureInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_owner_national_id_top', models.ImageField(blank=True, null=True, upload_to='users/national_id')),
                ('car_owner_national_id_down', models.ImageField(blank=True, null=True, upload_to='users/national_id')),
                ('driver_license_top', models.ImageField(blank=True, null=True, upload_to='users/driver_license')),
                ('driver_license_down', models.ImageField(blank=True, null=True, upload_to='users/driver_license')),
                ('road_worthiness_certificate_top', models.ImageField(blank=True, null=True, upload_to='users/road_worthiness_certificate')),
                ('road_worthiness_certificate_down', models.ImageField(blank=True, null=True, upload_to='users/road_worthiness_certificate')),
                ('insured_national_id_top', models.ImageField(blank=True, null=True, upload_to='users/driver_license')),
                ('insured_national_id_down', models.ImageField(blank=True, null=True, upload_to='users/driver_license')),
                ('last_year_enforced_insurance', models.ImageField(blank=True, null=True, upload_to='users/driver_license')),
                ('last_year_commercial_insurance', models.ImageField(blank=True, null=True, upload_to='users/driver_license')),
                ('jidongchejiaotongshifuzerenqiangzhibaoxian', models.BooleanField(default=False)),
                ('chechuanshiyongshui', models.BooleanField(default=False)),
                ('jidongchesunshibaoxian', models.BooleanField(default=False)),
                ('jidongchedisanzerenbaoxian', models.BooleanField(default=False)),
                ('jidongchecheshangrenyuanzerenbaoxian', models.BooleanField(default=False)),
                ('jidongchequanchedaoqiangbaoxian', models.BooleanField(default=False)),
                ('bolidanduposuixian', models.BooleanField(default=False)),
                ('ziransunshixian', models.BooleanField(default=False)),
                ('xinzengshebensunshixian', models.BooleanField(default=False)),
                ('cheshenhuahenshunshixian', models.BooleanField(default=False)),
                ('fadongjisheshuisunshixian', models.BooleanField(default=False)),
                ('xiuliqijianfeiyongbuchangxian', models.BooleanField(default=False)),
                ('cheshanghuowuzerenxian', models.BooleanField(default=False)),
                ('jingshensunhaifuxujinzerenxian', models.BooleanField(default=False)),
                ('bujimianpeilvxian', models.BooleanField(default=False)),
                ('jidongchesunshibaoxianwufazhaodaodisanfangteyuexian', models.BooleanField(default=False)),
                ('zhidingxiulichangxian', models.BooleanField(default=False)),
                ('insure_company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='insure.InsuranceCompanyForInsure')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='user.User')),
            ],
        ),
    ]
