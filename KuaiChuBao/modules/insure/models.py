# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class InsuranceCompanyForInsure(models.Model):
	name = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)
	url = models.CharField(max_length=200, null=True, blank=True)
	logo = models.ImageField(upload_to='companies_logo/', null=True, blank=True)

	# relations
	# 1. claims

	def __unicode__(self):
		return self.name


class InsureInfo(models.Model):
	# Step
	step = models.IntegerField(default=1)

	# Link
	user = models.ForeignKey('user.User', related_name='insures', on_delete=models.PROTECT)
	insure_company = models.ForeignKey(InsuranceCompanyForInsure, on_delete=models.PROTECT)

	# Images
	car_owner_national_id_top = models.ImageField(upload_to='users/national_id', null=True, blank=True)
	car_owner_national_id_down = models.ImageField(upload_to='users/national_id', null=True, blank=True)
	driver_license_top = models.ImageField(upload_to='users/driver_license', null=True, blank=True)
	driver_license_down = models.ImageField(upload_to='users/driver_license', null=True, blank=True)
	road_worthiness_certificate_top = models.ImageField(upload_to='users/road_worthiness_certificate', null=True, blank=True)
	road_worthiness_certificate_down = models.ImageField(upload_to='users/road_worthiness_certificate', null=True, blank=True)
	insured_national_id_top = models.ImageField(upload_to='users/driver_license', null=True, blank=True)
	insured_national_id_down = models.ImageField(upload_to='users/driver_license', null=True, blank=True)
	last_year_enforced_insurance = models.ImageField(upload_to='users/driver_license', null=True, blank=True)
	last_year_commercial_insurance = models.ImageField(upload_to='users/driver_license', null=True, blank=True)

	# Details
	jidongchejiaotongshifuzerenqiangzhibaoxian = models.BooleanField(default=False)
	chechuanshiyongshui = models.BooleanField(default=False)
	jidongchesunshibaoxian = models.BooleanField(default=False)
	jidongchedisanzerenbaoxian = models.BooleanField(default=False)
	jidongchecheshangrenyuanzerenbaoxian = models.BooleanField(default=False)
	jidongchequanchedaoqiangbaoxian = models.BooleanField(default=False)
	bolidanduposuixian = models.BooleanField(default=False)
	ziransunshixian = models.BooleanField(default=False)
	xinzengshebensunshixian = models.BooleanField(default=False)
	cheshenhuahenshunshixian = models.BooleanField(default=False)
	fadongjisheshuisunshixian = models.BooleanField(default=False)
	xiuliqijianfeiyongbuchangxian = models.BooleanField(default=False)
	cheshanghuowuzerenxian = models.BooleanField(default=False)
	jingshensunhaifuxujinzerenxian = models.BooleanField(default=False)
	bujimianpeilvxian = models.BooleanField(default=False)
	jidongchesunshibaoxianwufazhaodaodisanfangteyuexian = models.BooleanField(default=False)
	zhidingxiulichangxian = models.BooleanField(default=False)



	def __unicode__(self):
		return self.user.name + ' 投保信息'
