# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class User(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)
	phone = models.CharField(max_length=200, null=True, blank=True)
	national_id_number = models.CharField(max_length=200, unique=True)
	driver_license_number = models.CharField(max_length=200, null=True, blank=True)

	# relations
	# 1. claims

	def __unicode__(self):
		return self.name
