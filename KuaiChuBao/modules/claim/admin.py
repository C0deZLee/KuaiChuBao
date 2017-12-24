# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Claim, InsuranceCompany, Image, Location

admin.site.register(Claim)
admin.site.register(InsuranceCompany)
admin.site.register(Image)

