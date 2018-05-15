# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponseRedirect

from ..user.models import User


def insure_user(request):
	if request.method == 'GET':
		user_id = request.session.get('user_id')
		# 用户已经登陆
		if user_id:
			user_info = User.objects.get(id=request.session['user_id'])
			if user_info.insures.first():
				insure = user_info.insures.first()
				if insure.step == 1:
					return HttpResponseRedirect('/insure/')
				elif insure.step == 2:
					return HttpResponseRedirect('/insure/detail')
				elif insure.step == 3:
					return HttpResponseRedirect('/insure/company')
				elif insure.step == 4:
					return HttpResponseRedirect('/insure/complete')

			else:
				return HttpResponseRedirect('/insure/upload')
		# 用户没有登陆
		return render(request, 'insure_user_login.html')

	elif request.method == 'POST':
		if request.POST.get('name') and \
				request.POST.get('national_id') and \
				request.POST.get('phone'):

			user_info, create = User.objects.get_or_create(
				national_id_number=request.POST.get('national_id'),
				name=request.POST.get('name'),
				phone=request.POST.get('phone')
			)

			request.session['user_id'] = user_info.id
			if user_info.insures.all().first():
				insure = user_info.insures.all().first()
				if insure.step < 11:
					return HttpResponseRedirect('/insure/step1?step=' + str(insure.step))
				elif insure.step == 12:
					return HttpResponseRedirect('/insure/detail')
				elif insure.step == 13:
					return HttpResponseRedirect('/insure/company')
				else:
					return HttpResponseRedirect('/insure/complete')
			else:
				return HttpResponseRedirect('/insure/upload')


def insure_upload(request):
	pass


def insure_detail(request):
	pass


def insure_company(request):
	pass


def insure_complete(request):
	pass
