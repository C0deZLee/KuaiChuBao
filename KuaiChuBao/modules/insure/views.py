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
		if request.GET.get('new') and request.session.get('insure_info_id'):
			del request.session['insure_info_id']
			request.session.modified = True

		# 在url中获取type存入session
		if request.GET.get('accident_type'):
			request.session['accident_type'] = request.GET.get('accident_type')

		companies = InsuranceCompany.objects.all()

		return render(request, 'insure_chose_company.html',
		              {'companies': companies})

	elif request.method == 'POST':
		companies = []
		for form_data in request.POST:
			if '-check' in form_data:
				companies.append(InsuranceCompany.objects.get(id=form_data.split('-')[0]))
		if not companies:
			companies = InsuranceCompany.objects.all()
			return render(request, 'insure_chose_company.html',
			              {'error': '必须选择至少一个投保公司', 'companies': companies})

		# Check if user already has a insure and resume from there
		if not request.session.get('insure_info_id'):
			# 创建新的InsureInfo实例
			insure_info = InsureInfo.objects.create(
				step=2,
				user_id=request.session.get('user_id'),
			)
			for company in companies:
				insure_info.insure_company.add(company)

			insure_info.save()
			request.session['insure_info_id'] = insure_info.id
		else:
			insure_info = InsureInfo.objects.get(id=request.session.get('insure_info_id'))
			insure_info.insure_company.clear()
			for company in companies:
				insure_info.insure_company.add(company)
			insure_info.save()

		return HttpResponseRedirect('/insure/form')


def insure_form(request):
	# 重定向未登录用户
	if not request.session.get('user_id'):
		return HttpResponseRedirect('/insure')

	insure_info_id = request.session.get('insure_info_id')

	# 处理请求
	if request.method == 'GET':
		insure_info = InsureInfo.objects.get(id=insure_info_id)
		companies = insure_info.insure_company.all()

		return render(request, 'insure_form.html', {'companies': companies})

	elif request.method == 'POST':
		if not request.session.get('insure_info_id'):
			return HttpResponseRedirect('/insure/form')
		else:
			# 拉取InsureInfo实例
			insure_info = InsureInfo.objects.get(id=insure_info_id)

			insure_info.jidongchedisanzerenbaoxian = True if request.POST.get('jidongchedisanfangzerenbaoxian') else False
			insure_info.jidongchedisanzerenbaoxianbaoe = request.POST.get('jidongchedisanfangzerenbaoxianbaoe') if request.POST.get('jidongchedisanfangzerenbaoxian') else None

			insure_info.jidongchecheshangrenyuanzerenbaoxian = True if request.POST.get('jidongchecheshangrenyuanzerenbaoxian') else False
			insure_info.jidongchecheshangrenyuanzerenbaoxianbaoe = request.POST.get('jidongchecheshangrenyuanzerenbaoxianbaoe') if request.POST.get('jidongchecheshangrenyuanzerenbaoxian') else None

			insure_info.jidongchecheshangrenyuanzerenbaoxianchengke = True if request.POST.get('jidongchecheshangrenyuanzerenbaoxianchengke') else False
			insure_info.jidongchecheshangrenyuanzerenbaoxianchengkebaoe = request.POST.get('jidongchecheshangrenyuanzerenbaoxianchengkebaoe') if request.POST.get(
				'jidongchecheshangrenyuanzerenbaoxianchengke') else None

			insure_info.jidongcheshiguzerenqiangzhibaoxian = True if request.POST.get('jidongcheshiguzerenqiangzhibaoxian') else False
			insure_info.chechuanshiyongshui = True if request.POST.get('chechuanshiyongshui') else False
			insure_info.jidongchesunshibaoxian = True if request.POST.get('jidongchesunshibaoxian') else False
			insure_info.jidongchequanchedaoqiangbaoxian = True if request.POST.get('jidongchequanchedaoqiangbaoxian') else False
			insure_info.bolidanduposuixian = True if request.POST.get('bolidanduposuixian') else False
			insure_info.ziransunshixian = True if request.POST.get('ziransunshixian') else False
			insure_info.xinzengshebensunshixian = True if request.POST.get('xinzengshebensunshixian') else False
			insure_info.cheshenhuahenshunshixian = True if request.POST.get('cheshenhuahenshunshixian') else False
			insure_info.fadongjisheshuisunshixian = True if request.POST.get('fadongjisheshuisunshixian') else False
			insure_info.xiuliqijianfeiyongbuchangxian = True if request.POST.get('xiuliqijianfeiyongbuchangxian') else False
			insure_info.cheshanghuowuzerenxian = True if request.POST.get('cheshanghuowuzerenxian') else False
			insure_info.jingshensunhaifuxujinzerenxian = True if request.POST.get('jingshensunhaifuxujinzerenxian') else False
			insure_info.bujimianpeilvxian = True if request.POST.get('bujimianpeilvxian') else False
			insure_info.jidongchesunshibaoxianwufazhaodaodisanfangteyuexian = True if request.POST.get('jidongchesunshibaoxianwufazhaodaodisanfangteyuexian') else False
			insure_info.zhidingxiulichangxian = True if request.POST.get('zhidingxiulichangxian') else False
			insure_info.step = 3
			insure_info.save()

	return HttpResponseRedirect('/insure/upload')


def insure_upload(request):
	user_id = request.session.get('user_id')
	insure_id = request.session.get('insure_info_id')

	# 重定向未登录用户
	if not user_id:
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

		if img_upload_step == 9:
			return HttpResponseRedirect('/insure/finish')

		step_name = type_step[img_upload_step - 1]

		ctx = {'step'     : img_upload_step,
		       'step_name': step_name}

		return render(request, 'insure_img_upload.html', ctx)

	if request.method == 'POST':

		if request.FILES.get('insure_img'):
			if img_upload_step == 1:
				insure_instance.car_owner_national_id_top = request.FILES.get('insure_img')
			elif img_upload_step == 2:
				insure_instance.car_owner_national_id_down = request.FILES.get('insure_img')
			elif img_upload_step == 3:
				insure_instance.driver_license_top = request.FILES.get('insure_img')
			elif img_upload_step == 4:
				insure_instance.driver_license_down = request.FILES.get('insure_img')
			elif img_upload_step == 5:
				insure_instance.insured_national_id_top = request.FILES.get('insure_img')
			elif img_upload_step == 6:
				insure_instance.insured_national_id_down = request.FILES.get('insure_img')
			elif img_upload_step == 7:
				insure_instance.last_year_enforced_insurance = request.FILES.get('insure_img')
			elif img_upload_step == 8:
				insure_instance.last_year_commercial_insurance = request.FILES.get('insure_img')
				insure_instance.save()
				# 如果到了最后一步，跳转到结束页面
				return HttpResponseRedirect('/insure/finish')

			insure_instance.save()
			img_upload_step += 1
			request.session['img_upload_step'] = img_upload_step

			return HttpResponseRedirect('/insure/upload')
		else:
			img_upload_step += 1
			request.session['img_upload_step'] = img_upload_step
			return HttpResponseRedirect('/insure/upload?empty=true')


def insure_complete(request):
	return render(request, 'insure_finish.html')
