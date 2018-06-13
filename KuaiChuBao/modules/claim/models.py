# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class InsuranceCompany(models.Model):
	name = models.CharField(unique=True, max_length=200, verbose_name='名字')
	phone = models.CharField(max_length=200, verbose_name='电话号码')
	url = models.CharField(max_length=200, null=True, blank=True, verbose_name='公司网址')
	logo = models.ImageField(upload_to='companies_logo/', null=True, blank=True, verbose_name='公司Logo')

	# relations
	# 1. claims

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = '保险公司'
		verbose_name_plural = '保险公司'


class Location(models.Model):
	x = models.FloatField(default=0.0)
	y = models.FloatField(default=0.0)
	z = models.FloatField(default=0.0)

	def __unicode__(self):
		return self.id

	class Meta:
		verbose_name = '事发地点'
		verbose_name_plural = '事发地点'


class Claim(models.Model):
	TYPE_CHOICES = (
		('danche', '单车事故'),
		('guaca', '两车刮擦事故'),
		('zhuiwei', '两车追尾事故'),
	)
	company = models.ForeignKey(InsuranceCompany, related_name='claims', verbose_name='投保公司')
	accident_type = models.CharField(choices=TYPE_CHOICES, max_length=20, verbose_name='出险类型')
	user = models.ForeignKey('user.User', related_name='claims', verbose_name='用户')

	car_plate = models.CharField(max_length=200, verbose_name='车牌号')
	time = models.CharField(max_length=200, verbose_name='出险时间')
	location = models.CharField(max_length=200, verbose_name='出险地点')

	step = models.IntegerField(default=1)

	# time stamp
	created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

	# relations
	# 1. images

	def __unicode__(self):
		return self.user.name + ' ' + self.created.strftime('%Y-%m-%d %H:%M')

	class Meta:
		verbose_name = '出险记录'
		verbose_name_plural = '出险记录'


class Image(models.Model):
	name = models.CharField(max_length=120, verbose_name='图像名称')
	claim = models.ForeignKey(Claim, related_name='images', verbose_name='出险记录')
	image = models.ImageField(upload_to='claims', verbose_name='图像记录')
	step = models.IntegerField(verbose_name='步骤')

	# Time stamp
	created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

	def __unicode__(self):
		return self.claim.user.name + ' ' + self.created.strftime('%Y-%m-%d %H:%M') + ' image'

	class Meta:
		verbose_name = '出险记录图片'
		verbose_name_plural = '出险记录图片'
