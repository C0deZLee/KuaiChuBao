# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import InsureInfo


@admin.register(InsureInfo)
class InsureInfoAdmin(admin.ModelAdmin):
	# List display Settings
	list_display = ('id', 'user', 'created',)
	search_fields = ('user',)
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
		                     'car_owner_national_id_down',
		                     'driver_license_top',
		                     'driver_license_down',
		                     'insured_national_id_top',
		                     'insured_national_id_down',
		                     'last_year_enforced_insurance',
		                     'last_year_commercial_insurance',)}),
		('时间戳', {'fields': ('created',)}),
		('Step', {'fields': ('step',)}),
	)
	readonly_fields = ('created',)
