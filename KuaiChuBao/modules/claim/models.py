# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class UserInfo(models.Model):
	name = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)
	national_id_number = models.CharField(max_length=200)
	driver_license_number = models.CharField(max_length=200)

	national_id_copy_top = models.ImageField(upload_to='users/national_id')
	national_id_copy_down = models.ImageField(upload_to='users/national_id')
	driver_license_copy_top = models.ImageField(upload_to='users/driver_license')
	driver_license_copy_down = models.ImageField(upload_to='users/driver_license')

	# relations
	# 1. claims

	def __str__(self):
		return self.name


class InsuranceCompany(models.Model):
	name = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)
	url = models.CharField(max_length=200)

	# relations
	# 1. claims

	def __str__(self):
		return self.name


class Location(models.Model):
	pass


class Claim(models.Model):
	TYPE_CHOICES = (
		(1, '单车事故'),
		(2, '两车刮擦事故'),
		(3, '两车追尾事故'),
	)
	company = models.ForeignKey(InsuranceCompany, related_name='claims')
	plate = models.CharField(max_length=200)
	time = models.DateTimeField(max_length=200)
	location = models.CharField(max_length=200)
	user = models.ForeignKey(UserInfo, related_name='claims')
	# time stamp
	created = models.DateTimeField(auto_now_add=True)

	# relations
	# 1. images

	def __str__(self):
		return self.user.name + ' ' + self.created.strftime('%Y-%m-%d %H:%M')


class Image(models.Model):
	claim = models.ForeignKey(Claim, related_name='images')
	image = models.ImageField(upload_to='claims')
	# time stamp
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.claim.user.name + ' ' + self.created.strftime('%Y-%m-%d %H:%M') + ' image'
