# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from ..claim.models import InsuranceCompany


class InsureInfo(models.Model):
	# Step
	step = models.IntegerField(default=1)

	# Link
	user = models.ForeignKey('user.User', related_name='insures', on_delete=models.PROTECT, verbose_name='用户')
	insure_company = models.ManyToManyField(InsuranceCompany, verbose_name='保险公司')

	# Images
	car_owner_national_id_top = models.ImageField(upload_to='insure/national_id', null=True, blank=True, verbose_name='车主身份证（正面）')
	car_owner_national_id_down = models.ImageField(upload_to='insure/national_id', null=True, blank=True, verbose_name='车主身份证（反面）')
	driver_license_top = models.ImageField(upload_to='insure/driver_license', null=True, blank=True, verbose_name='行驶证正本')
	driver_license_down_top = models.ImageField(upload_to='insure/driver_license', null=True, blank=True, verbose_name='行驶证副本（正面）')
	driver_license_down_down = models.ImageField(upload_to='insure/driver_license', null=True, blank=True, verbose_name='行驶证副本（反面）')
	insured_national_id_top = models.ImageField(upload_to='insure/national_id', null=True, blank=True, verbose_name='被保险人身份证（正面）')
	insured_national_id_down = models.ImageField(upload_to='insure/national_id', null=True, blank=True, verbose_name='被保险人身份证（反面）')
	last_year_enforced_insurance = models.ImageField(upload_to='insure/insurance', null=True, blank=True, verbose_name='去年交强险保单')
	last_year_commercial_insurance = models.ImageField(upload_to='insure/insurance', null=True, blank=True, verbose_name='去年商业险保单')

	# Details
	contact_phone = models.TextField(null=True, blank=True, verbose_name='联系电话')
	jidongchedisanzerenbaoxian = models.BooleanField(default=False, verbose_name='机动车第三者责任保险')
	jidongchecheshangrenyuanzerenbaoxian = models.BooleanField(default=False, verbose_name='机动车车上人员责任保险（司机）')
	jidongchecheshangrenyuanzerenbaoxianchengke = models.BooleanField(default=False, verbose_name='机动车车上人员责任保险（乘客）')

	jidongchedisanzerenbaoxianbaoe = models.CharField(max_length=100, null=True, blank=True, verbose_name='机动车第三者责任保险 保额')
	jidongchecheshangrenyuanzerenbaoxianbaoe = models.CharField(max_length=100, null=True, blank=True, verbose_name='机动车车上人员责任保险（司机） 保额')
	jidongchecheshangrenyuanzerenbaoxianchengkebaoe = models.CharField(max_length=100, null=True, blank=True, verbose_name='机动车车上人员责任保险（乘客） 保额')

	jidongcheshiguzerenqiangzhibaoxian = models.BooleanField(default=False, verbose_name='机动车事故责任强制险')
	chechuanshiyongshui = models.BooleanField(default=False, verbose_name='车船使用税')
	jidongchesunshibaoxian = models.BooleanField(default=False, verbose_name='机动车损失保险')
	jidongchequanchedaoqiangbaoxian = models.BooleanField(default=False, verbose_name='机动车全车抢盗保险')
	bolidanduposuixian = models.BooleanField(default=False, verbose_name='玻璃单独破碎保险')
	ziransunshixian = models.BooleanField(default=False, verbose_name='自燃损失险')
	xinzengshebensunshixian = models.BooleanField(default=False, verbose_name='新加设备损失险')

	cheshenhuahenshunshixian = models.BooleanField(default=False, verbose_name='车身划痕损失险')
	fadongjisheshuisunshixian = models.BooleanField(default=False, verbose_name='发动机涉水损失险')
	xiuliqijianfeiyongbuchangxian = models.BooleanField(default=False, verbose_name='修理期间费用补偿险')
	cheshanghuowuzerenxian = models.BooleanField(default=False, verbose_name='车上货物损失险')
	jingshensunhaifuxujinzerenxian = models.BooleanField(default=False, verbose_name='精神损害抚恤金险')
	bujimianpeilvxian = models.BooleanField(default=False, verbose_name='不计免赔率险')
	jidongchesunshibaoxianwufazhaodaodisanfangteyuexian = models.BooleanField(default=False, verbose_name='机动车损失无法找到第三方特约险')
	zhidingxiulichangxian = models.BooleanField(default=False, verbose_name='指定修理厂险')

	# Time stamp
	created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

	def __unicode__(self):
		return self.user.name + ' 投保信息'

	class Meta:
		verbose_name = '投保信息'
		verbose_name_plural = '投保信息'
