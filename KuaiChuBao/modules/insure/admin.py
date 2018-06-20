# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.html import mark_safe

from .models import InsureInfo


@admin.register(InsureInfo)
class InsureInfoAdmin(admin.ModelAdmin):
	# List display Settings
	list_display = ('id', 'user', 'created',)
	search_fields = ('user__name', 'created',)
	ordering = ('created',)

	# Detail Page Settings
	fieldsets = (
		('', {'fields': ('user', 'insure_company',)}),
		('投保信息', {'fields': ('jidongchedisanzerenbaoxian',
		                     'jidongchedisanzerenbaoxianbaoe',
		                     'jidongchecheshangrenyuanzerenbaoxian',
		                     'jidongchecheshangrenyuanzerenbaoxianbaoe',
		                     'jidongchecheshangrenyuanzerenbaoxianchengke',
		                     'jidongchecheshangrenyuanzerenbaoxianchengkebaoe',
		                     'jidongcheshiguzerenqiangzhibaoxian',
		                     'chechuanshiyongshui',
		                     'jidongchesunshibaoxian',
		                     'jidongchequanchedaoqiangbaoxian',
		                     'bolidanduposuixian',
		                     'ziransunshixian',
		                     'xinzengshebensunshixian',
		                     'cheshenhuahenshunshixian',
		                     'fadongjisheshuisunshixian',
		                     'xiuliqijianfeiyongbuchangxian',
		                     'cheshanghuowuzerenxian',
		                     'jingshensunhaifuxujinzerenxian',
		                     'bujimianpeilvxian',
		                     'jidongchesunshibaoxianwufazhaodaodisanfangteyuexian',
		                     'zhidingxiulichangxian')}),
		('文件资料', {'fields': ('car_owner_national_id_top',
		                     'car_owner_national_id_top_tag',
		                     'car_owner_national_id_down',
		                     'car_owner_national_id_down_tag',
		                     'driver_license_top',
		                     'driver_license_top_tag',
		                     'driver_license_down',
		                     'driver_license_down_tag',
		                     'insured_national_id_top',
		                     'insured_national_id_top_tag',
		                     'insured_national_id_down',
		                     'insured_national_id_down_tag',
		                     'last_year_enforced_insurance',
		                     'last_year_enforced_insurance_tag',
		                     'last_year_commercial_insurance',
		                     'last_year_commercial_insurance_tag',)}),
		('时间戳', {'fields': ('created',)}),
		('Step', {'fields': ('step',)}),
	)
	readonly_fields = ('created', 'car_owner_national_id_top_tag', 'car_owner_national_id_down_tag',
	                   'driver_license_top_tag', 'driver_license_down_tag', 'insured_national_id_top_tag', 'insured_national_id_down_tag',
	                   'last_year_enforced_insurance_tag', 'last_year_commercial_insurance_tag')

	def car_owner_national_id_top_tag(self, obj):
		return mark_safe(u'<img src="' + obj.car_owner_national_id_top.url + '" style="width:20%;height:20%" />')

	def car_owner_national_id_down_tag(self, obj):
		return mark_safe(u'<img src="' + obj.car_owner_national_id_down.url + '" style="width:20%;height:20%" />')

	def driver_license_top_tag(self, obj):
		return mark_safe(u'<img src="' + obj.driver_license_top.url + '" style="width:20%;height:20%" />')

	def driver_license_down_tag(self, obj):
		return mark_safe(u'<img src="' + obj.driver_license_down.url + '" style="width:20%;height:20%" />')

	def insured_national_id_top_tag(self, obj):
		return mark_safe(u'<img src="' + obj.insured_national_id_top.url + '" style="width:20%;height:20%" />')

	def insured_national_id_down_tag(self, obj):
		return mark_safe(u'<img src="' + obj.insured_national_id_down.url + '" style="width:20%;height:20%" />')

	def last_year_enforced_insurance_tag(self, obj):
		return mark_safe(u'<img src="' + obj.last_year_enforced_insurance.url + '" style="width:20%;height:20%" />')

	def last_year_commercial_insurance_tag(self, obj):
		return mark_safe(u'<img src="' + obj.last_year_commercial_insurance.url + '" style="width:20%;height:20%" />')

	car_owner_national_id_top_tag.short_description = '车主身份证（正面）缩略图'
	car_owner_national_id_down_tag.short_description = '车主身份证（反面）缩略图'
	driver_license_top_tag.short_description = '行驶证正本缩略图'
	driver_license_down_tag.short_description = '行驶证副本缩略图'
	insured_national_id_top_tag.short_description = '被保险人身份证（正面）缩略图'
	insured_national_id_down_tag.short_description = '被保险人身份证（反面）缩略图'
	last_year_enforced_insurance_tag.short_description = '去年交强险保单缩略图'
	last_year_commercial_insurance_tag.short_description = '去年商业险保单缩略图'
