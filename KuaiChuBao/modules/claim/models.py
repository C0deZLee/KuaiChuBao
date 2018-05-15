# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class InsuranceCompany(models.Model):
	name = models.CharField(unique=True, max_length=200)
	phone = models.CharField(max_length=200)
	url = models.CharField(max_length=200, null=True, blank=True)
	logo = models.ImageField(upload_to='companies_logo/', null=True, blank=True)

	# relations
	# 1. claims

	def __unicode__(self):
		return self.name


class Location(models.Model):
	x = models.FloatField(default=0.0)
	y = models.FloatField(default=0.0)
	z = models.FloatField(default=0.0)

	def __unicode__(self):
		return self.id


class Claim(models.Model):
	TYPE_CHOICES = (
		('danche', '单车事故'),
		('guaca', '两车刮擦事故'),
		('zhuiwei', '两车追尾事故'),
	)
	company = models.ForeignKey(InsuranceCompany, related_name='claims')
	accident_type = models.CharField(choices=TYPE_CHOICES, max_length=20)
	user = models.ForeignKey('user.User', related_name='claims')

	car_plate = models.CharField(max_length=200)
	time = models.CharField(max_length=200)
	location = models.CharField(max_length=200)

	step = models.IntegerField(default=1)
	# time stamp
	created = models.DateTimeField(auto_now_add=True)

	# relations
	# 1. images

	def __unicode__(self):
		return self.user.name + ' ' + self.created.strftime('%Y-%m-%d %H:%M')


class Image(models.Model):
	claim = models.ForeignKey(Claim, related_name='images')
	image = models.ImageField(upload_to='claims')
	step = models.IntegerField()
	# time stamp
	created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.claim.user.name + ' ' + self.created.strftime('%Y-%m-%d %H:%M') + ' image'
