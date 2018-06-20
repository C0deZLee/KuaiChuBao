# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.html import mark_safe
from django.contrib.auth.models import Permission
from django.contrib import admin

from .models import Claim, InsuranceCompany, Image, Location

admin.site.register(InsuranceCompany)


class ImageInline(admin.TabularInline):
	model = Image
	show_change_link = True
	fields = ('step', 'name', 'image', 'image_tag', 'created',)
	readonly_fields = ('step', 'name', 'image_tag', 'created')
	extra = 0

	def image_tag(self, obj):
		return mark_safe(u'<img src="' + obj.image.url + '" style="width:50%;height:50%" />')

	image_tag.short_description = '图像缩略图'


@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
	def get_queryset(self, request):
		qs = super(ClaimAdmin, self).get_queryset(request)
		if request.user.is_superuser:
			return qs
		# if request.user.has_perm:
		return qs.filter(company__name='Demo1')

	# List display Settings
	list_display = ('id', 'user', 'company', 'time', 'car_plate', 'location',)
	search_fields = ('user__name', 'company__name', 'time', 'car_plate', 'location')
	ordering = ('created',)

	# Detail Page Settings
	fieldsets = (
		('', {'fields': ('user', 'company', 'accident_type')}),
		('出险信息', {'fields': ('car_plate', 'time', 'location',)}),
		('时间戳', {'fields': ('created',)}),
	)
	readonly_fields = ('created',)

	inlines = [ImageInline, ]


admin.site.register(Permission)
