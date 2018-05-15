# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import urllib

from django.shortcuts import render

from django.http import HttpResponseRedirect

from ..user.models import User
from ..claim.models import InsuranceCompany
from models import InsureInfo


def insure_user(request):
	if request.method == 'GET':
		user_id = request.session.get('user_id')
		# 用户已经登陆
		if user_id:
			user_info = User.objects.get(id=request.session['user_id'])
			if user_info.insures.first():
				insure = user_info.insures.first()
				if insure.step == 1:
					return HttpResponseRedirect('/insure/company')
				elif insure.step == 2:
					return HttpResponseRedirect('/insure/form')
				elif insure.step == 3:
					return HttpResponseRedirect('/insure/upload')
				elif insure.step == 4:
					return HttpResponseRedirect('/insure/complete')

			else:
				return HttpResponseRedirect('/insure/company')
		# 用户没有登陆
		return render(request, 'insure_user_login.html')

	elif request.method == 'POST':
		if request.POST.get('name') and \
				request.POST.get('national_id') and \
				request.POST.get('phone'):

			user_info = User.objects.filter(national_id_number=request.POST.get('national_id'))
			if user_info:
				user_info = user_info[0]
			else:
				user_info, create = User.objects.get_or_create(
					national_id_number=request.POST.get('national_id'),
					name=request.POST.get('name'),
					phone=request.POST.get('phone')
				)

			request.session['user_id'] = user_info.id
			if user_info.insures.all().first():
				insure = user_info.insures.all().first()
				if insure.step == 1:
					return HttpResponseRedirect('/insure/company')
				elif insure.step == 2:
					return HttpResponseRedirect('/insure/form')
				elif insure.step == 3:
					return HttpResponseRedirect('/insure/upload')
				elif insure.step == 4:
					return HttpResponseRedirect('/insure/complete')
			else:
				return HttpResponseRedirect('/insure/company')


def insure_company(request):
	# 重定向未登录用户
	if not request.session.get('user_id'):
		return HttpResponseRedirect('/insure')

	if request.method == 'GET':
		# 在url中获取type存入session
		if request.GET.get('accident_type'):
			request.session['accident_type'] = request.GET.get('accident_type')

		companies = InsuranceCompany.objects.all()

		return render(request, 'insure_chose_company.html',
		              {'companies': companies})


def insure_form(request):
	# 重定向未登录用户
	if not request.session.get('user_id'):
		return HttpResponseRedirect('/insure')

	# 重定向没有选公司的用户
	if (not request.GET.get('company')) and (not request.session['company']):
		return HttpResponseRedirect('/insure')

	if request.method == 'GET':
		# 在url中获取type存入session
		if not request.session.get('company') or request.GET.get('company'):
			request.session['company'] = request.GET.get('company')

		company = InsuranceCompany.objects.get(name=urllib.unquote(request.session['company']))

		# Check if user already has a insure and resume from there
		if not request.session.get('insureinfo_id'):
			# 创建新的InsureInfo实例
			insureinfo = InsureInfo.objects.create(
				step=2,
				user_id=request.session.get('user_id'),
				insure_company=company
			)
			request.session['insureinfo_id'] = insureinfo.id

		return render(request, 'insure_form.html', {'company': request.session['company']})

	elif request.method == 'POST':
		# TODO: Do the form recording
		return HttpResponseRedirect('/insure/upload')


def insure_upload(request):
	user_id = request.session.get('user_id')
	company = request.session.get('company')
	insure_id = request.session.get('insureinfo_id')

	# 重定向未登录用户
	if not user_id:
		return HttpResponseRedirect('/insure')

	# 重定向无company用户
	if not company and not request.GET.get('company'):
		return HttpResponseRedirect('/insure')

	# 重定向无insure_id用户
	if not insure_id:
		return HttpResponseRedirect('/insure')

	img_upload_step = request.session.get('img_upload_step', 1)
	insure_instance = InsureInfo.objects.get(id=insure_id)

	type_step = ['上传车主身份证（正面）',
	             '上传车主身份证（反面）',
	             '上传行驶证正本',
	             '上传行驶证副本',
	             '上传被保险人身份证（正面）',
	             '上传被保险人身份证（反面）',
	             '上传去年交强险保单',
	             '上传去年商业险保单'
	             ]
	if request.method == 'GET':
		# Perform Back
		if request.GET.get('back'):
			if img_upload_step == 1:
				return HttpResponseRedirect('/insure/form')
			else:
				img_upload_step -= 1
				request.session['img_upload_step'] = img_upload_step
				step_name = type_step[img_upload_step - 1]

				return render(request, 'insure_img_upload.html', {'step'     : img_upload_step,
				                                                  'step_name': step_name})

		# Create context
		step_name = type_step[img_upload_step - 1]

		ctx = {'step'     : img_upload_step,
		       'step_name': step_name}

		if request.GET.get('empty'):
			ctx['error_msg'] = '图片不得为空'

		return render(request, 'insure_img_upload.html', ctx)

	if request.method == 'POST':

		# 如果到了最后一步，跳转到结束页面
		if img_upload_step == 8:
			return HttpResponseRedirect('/insure/finish')

		if request.FILES.get('insure_img'):
			if img_upload_step == 0:
				insure_instance.car_owner_national_id_top = request.FILES.get('insure_img')
			elif img_upload_step == 1:
				insure_instance.car_owner_national_id_down = request.FILES.get('insure_img')

			insure_instance.save()
			img_upload_step += 1
			request.session['img_upload_step'] = img_upload_step

			return HttpResponseRedirect('/insure/upload')
		else:
			return HttpResponseRedirect('/insure/upload?empty=true')


def insure_complete(request):
	return render(request, 'insure_finish.html')
