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
		if not request.user.has_perm('claim.can_view_ya'):
			qs = qs.exclude(company__name='永安财险')
		if not request.user.has_perm('claim.can_view_ga'):
			qs = qs.exclude(company__name='国元财险')
		if not request.user.has_perm('claim.can_view_yc'):
			qs = qs.exclude(company__name='永诚财险')
		if not request.user.has_perm('claim.can_view_jt'):
			qs = qs.exclude(company__name='锦泰财险')
		if not request.user.has_perm('claim.can_view_ac'):
			qs = qs.exclude(company__name='安诚财险')
		if not request.user.has_perm('claim.can_view_de'):
			qs = qs.exclude(company__name='鼎和财险')
		if not request.user.has_perm('claim.can_view_ha'):
			qs = qs.exclude(company__name='华安财险')
		if not request.user.has_perm('claim.can_view_gs'):
			qs = qs.exclude(company__name='国寿财险')
		if not request.user.has_perm('claim.can_view_dd'):
			qs = qs.exclude(company__name='大地财险')
		if not request.user.has_perm('claim.can_view_yg'):
			qs = qs.exclude(company__name='阳光财险')
		if not request.user.has_perm('claim.can_view_tb'):
			qs = qs.exclude(company__name='太保财险')
		if not request.user.has_perm('claim.can_view_pa'):
			qs = qs.exclude(company__name='平安财险')
		if not request.user.has_perm('claim.can_view_rb'):
			qs = qs.exclude(company__name='人保财险')
		return qs

	# List display Settings
	list_display = ('id', 'user', 'company', 'time', 'car_plate', 'location', 'insured_person', 'driver', 'contact_phone')

	search_fields = ('user__name', 'company__name', 'time', 'car_plate', 'location')
	ordering = ('-created',)

	# Detail Page Settings
	fieldsets = (
		('', {'fields': ('user', 'company', 'accident_type')}),
		('出险信息', {'fields': ('car_plate', 'time', 'location',)}),
		('时间戳', {'fields': ('created',)}),
	)
	readonly_fields = ('created',)

	inlines = [ImageInline, ]


admin.site.register(Permission)
