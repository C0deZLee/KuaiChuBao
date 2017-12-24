# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import InsuranceCompanyForInsure, InsureInfo

admin.site.register(InsureInfo)
admin.site.register(InsuranceCompanyForInsure)

