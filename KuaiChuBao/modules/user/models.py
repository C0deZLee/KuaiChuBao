# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class User(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True, verbose_name='姓名')
	phone = models.CharField(max_length=200, null=True, blank=True, verbose_name='电话')
	national_id_number = models.CharField(max_length=200, unique=True, verbose_name='身份证号码')

	# relations
	# 1. claims

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = '车帮手用户'
		verbose_name_plural = '车帮手用户'
