# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-26 20:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insure', '0002_auto_20180515_1422'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='insureinfo',
            options={'verbose_name': '\u6295\u4fdd\u4fe1\u606f', 'verbose_name_plural': '\u6295\u4fdd\u4fe1\u606f'},
        ),
        migrations.RemoveField(
            model_name='insureinfo',
            name='jidongchejiaotongshifuzerenqiangzhibaoxian',
        ),
        migrations.RemoveField(
            model_name='insureinfo',
            name='road_worthiness_certificate_down',
        ),
        migrations.RemoveField(
            model_name='insureinfo',
            name='road_worthiness_certificate_top',
        ),
        migrations.AddField(
            model_name='insureinfo',
            name='jidongcheshiguzerenqiangzhibaoxian',
            field=models.BooleanField(default=False, verbose_name='\u673a\u52a8\u8f66\u4e8b\u6545\u8d23\u4efb\u5f3a\u5236\u9669'),
        ),
        migrations.AlterField(
            model_name='insureinfo',
            name='bolidanduposuixian',
            field=models.BooleanField(default=False, verbose_name='\u73bb\u7483\u5355\u72ec\u7834\u788e\u4fdd\u9669'),
        ),
        migrations.AlterField(
            model_name='insureinfo',
            name='bujimianpeilvxian',
            field=models.BooleanField(default=False, verbose_name='\u4e0d\u8ba1\u514d\u8d54\u7387\u9669'),
        ),
        migrations.AlterField(
            model_name='insureinfo',
            name='car_owner_national_id_down',
            field=models.ImageField(blank=True, null=True, upload_to='users/national_id', verbose_name='\u8f66\u4e3b\u8eab\u4efd\u8bc1\uff08\u53cd\u9762\uff09'),
        ),
        migrations.AlterField(
            model_name='insureinfo',
            name='car_owner_national_id_top',
            field=models.ImageField(blank=True, null=True, upload_to='users/national_id', verbose_name='\u8f66\u4e3b\u8eab\u4efd\u8bc1\uff08\u6b63\u9762\uff09'),
        ),
        migrations.AlterField(
            model_name='insureinfo',
            name='chechuanshiyongshui',
            field=models.BooleanField(default=False, verbose_name='\u8f66\u8239\u4f7f\u7528\u7a0e'),
        ),
        migrations.AlterField(
            model_name='insureinfo',
            name='cheshanghuowuzerenxian',
            field=models.BooleanField(default=False, verbose_name='\u8f66\u4e0a\u8d27\u7269\u635f\u5931\u9669'),
        ),
        migrations.AlterField(
            model_name='insureinfo',
            name='cheshenhuahenshunshixian',
            field=models.BooleanField(default=False, verbose_name='\u8f66\u8eab\u5212\u75d5\u635f\u5931\u9669'),
        ),
        migrations.AlterField(
            model_name='insureinfo',
            name='driver_license_down',
            field=models.ImageField(blank=True, null=True, upload_to='users/driver_license', verbose_name='\u884c\u9a76\u8bc1\u526f\u672c'),
        ),
        migrations.AlterField(
            model_name='insureinfo',
            name='driver_license_top',
            field=models.ImageField(blank=True, null=True, upload_to='users/driver_license', verbose_name='\u884c\u9a76\u8bc1\u6b63\u672c'),
        ),
        migrations.AlterField(
            model_name='insureinfo',
            name='fadongjisheshuisunshixian',
            field=models.BooleanField(default=False, verbose_name='\u53d1\u52a8\u673a\u6d89\u6c34\u635f\u5931\u9669'),
        ),
        migrations.AlterField(
            model_name='insureinfo',
            name='insure_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='claim.InsuranceCompany', verbose_name='\u4fdd\u9669\u516c\u53f8'),
        ),
        migrations.AlterField(
            model_name='insureinfo',
            name='insured_national_id_down',
            field=models.ImageField(blank=True, null=True, upload_to='users/road_worthiness_certificate', verbose_name='\u88ab\u4fdd\u9669\u4eba\u8eab\u4efd\u8bc1\uff08\u53cd\u9762\uff09'),
        ),
        migrations.AlterField(
            model_name='insureinfo',
            name='insured_national_id_top',
            field=models.ImageField(blank=True, null=True, upload_to='users/road_worthiness_certificate', verbose_name='\u88ab\u4fdd\u9669\u4eba\u8eab\u4efd\u8bc1\uff08\u6b63\u9762\uff09'),
        ),
        migrations.AlterField(
            model_name='insureinfo',
            name='jidongchecheshangrenyuanzerenbaoxian',
            field=models.IntegerField(verbose_name='\u673a\u52a8\u8f66\u8f66\u4e0a\u4eba\u5458\u8d23\u4efb\u4fdd\u9669'),
        ),
        migrations.AlterField(
            model_name='insureinfo',
            name='jidongchedisanzerenbaoxian',
            field=models.IntegerField(verbose_name='\u673a\u52a8\u8f66\u7b2c\u4e09\u8005\u8d23\u4efb\u4fdd\u9669'),
        ),
        migrations.AlterField(
            model_name='insureinfo',
            name='jidongchequanchedaoqiangbaoxian',
            field=models.BooleanField(default=False, verbose_name='\u673a\u52a8\u8f66\u5168\u8f66\u62a2\u76d7\u4fdd\u9669'),
        ),
        migrations.AlterField(
            model_name='insureinfo',
            name='jidongchesunshibaoxian',
            field=models.BooleanField(default=False, verbose_name='\u673a\u52a8\u8f66\u635f\u5931\u4fdd\u9669'),
        ),
        migrations.AlterField(
            model_name='insureinfo',
            name='jidongchesunshibaoxianwufazhaodaodisanfangteyuexian',
            field=models.BooleanField(default=False, verbose_name='\u673a\u52a8\u8f66\u635f\u5931\u65e0\u6cd5\u627e\u5230\u7b2c\u4e09\u65b9\u7279\u7ea6\u9669'),
        ),
        migrations.AlterField(
            model_name='insureinfo',
            name='jingshensunhaifuxujinzerenxian',
            field=models.BooleanField(default=False, verbose_name='\u7cbe\u795e\u635f\u5bb3\u629a\u6064\u91d1\u9669'),
        ),
        migrations.AlterField(
            model_name='insureinfo',
            name='last_year_commercial_insurance',
            field=models.ImageField(blank=True, null=True, upload_to='users/driver_license', verbose_name='\u53bb\u5e74\u5546\u4e1a\u9669\u4fdd\u5355'),
        ),
        migrations.AlterField(
            model_name='insureinfo',
            name='last_year_enforced_insurance',
            field=models.ImageField(blank=True, null=True, upload_to='users/driver_license', verbose_name='\u53bb\u5e74\u4ea4\u5f3a\u9669\u4fdd\u5355'),
        ),
        migrations.AlterField(
            model_name='insureinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='insures', to='user.User', verbose_name='\u7528\u6237'),
        ),
        migrations.AlterField(
            model_name='insureinfo',
            name='xinzengshebensunshixian',
            field=models.BooleanField(default=False, verbose_name='\u65b0\u52a0\u8bbe\u5907\u635f\u5931\u9669'),
        ),
        migrations.AlterField(
            model_name='insureinfo',
            name='xiuliqijianfeiyongbuchangxian',
            field=models.BooleanField(default=False, verbose_name='\u4fee\u7406\u671f\u95f4\u8d39\u7528\u8865\u507f\u9669'),
        ),
        migrations.AlterField(
            model_name='insureinfo',
            name='zhidingxiulichangxian',
            field=models.BooleanField(default=False, verbose_name='\u6307\u5b9a\u4fee\u7406\u5382\u9669'),
        ),
        migrations.AlterField(
            model_name='insureinfo',
            name='ziransunshixian',
            field=models.BooleanField(default=False, verbose_name='\u81ea\u7136\u635f\u5931\u9669'),
        ),
        migrations.DeleteModel(
            name='InsuranceCompanyForInsure',
        ),
    ]