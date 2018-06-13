# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Claim, InsuranceCompany, Image, Location

admin.site.register(InsuranceCompany)


class ImageInline(admin.TabularInline):
	model = Image
	show_change_link = True
	fields = ('step', 'name', 'image', 'created',)
	readonly_fields = ('step', 'name', 'created')
	extra = 0


@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
	# List display Settings
	list_display = ('id', 'user', 'company', 'time', 'car_plate', 'location',)
	search_fields = ('user', 'company')
	ordering = ('created',)

	# Detail Page Settings
	fieldsets = (
		('', {'fields': ('user', 'company', 'accident_type')}),
		('出险信息', {'fields': ('car_plate', 'time', 'location',)}),
		('时间戳', {'fields': ('created',)}),
	)
	readonly_fields = ('created',)

	inlines = [ImageInline, ]
