# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponseRedirect

from .models import InsuranceCompany, Claim, Image

from ..user.models import User


def claim_user(request):
	if request.method == 'GET':
		user_id = request.session.get('user_id')
		# 用户已经登陆
		if user_id:
			user_info = User.objects.get(id=request.session['user_id'])
			if user_info.claims.all():
				return HttpResponseRedirect('/claim/new_or_resume')
			else:
				return HttpResponseRedirect('/claim/type')

		return render(request, 'claim_user_login.html')

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
			if user_info.claims.all():
				return HttpResponseRedirect('/claim/new_or_resume')
			else:
				return HttpResponseRedirect('/claim/type')


def claim_new_or_resume(request):
	# 重定向未登录用户
	if not request.session.get('user_id'):
		return HttpResponseRedirect('/claim')

	return render(request, 'claim_new_or_resume.html')


def claim_resume(request):
	# 重定向未登录用户
	if not request.session.get('user_id'):
		return HttpResponseRedirect('/claim')

	user = User.objects.get(id=request.session.get('user_id'))

	return render(request, 'claim_resume.html', {'claims': user.claims.all()})


def claim_chose_accident_type(request):
	# 重定向未登录用户
	if not request.session.get('user_id'):
		return HttpResponseRedirect('/claim')

	if request.method == 'GET':
		return render(request, 'claim_chose_accident_type.html')


def claim_chose_company(request):
	# 重定向未登录用户
	if not request.session.get('user_id'):
		return HttpResponseRedirect('/claim')

	# 重定向无type用户
	if not request.session.get('accident_type') and not request.GET.get('accident_type'):
		return HttpResponseRedirect('/claim')

	if request.method == 'GET':
		# 在url中获取type存入session
		if request.GET.get('accident_type'):
			request.session['accident_type'] = request.GET.get('accident_type')

		companies = InsuranceCompany.objects.all()

		return render(request, 'claim_chose_company.html', {'companies': companies, 'accident_type': request.session['accident_type']})  # def claim_landing(request):


def claim_fill_claim(request):
	# 重定向未登录用户
	if not request.session.get('user_id'):
		return HttpResponseRedirect('/claim')

	# 重定向无type用户
	if not request.session.get('accident_type'):
		return HttpResponseRedirect('/claim')

	# 重定向无company用户
	if not request.session.get('company') and not request.GET.get('company'):
		return HttpResponseRedirect('/claim')

	if request.method == 'GET':
		# 在url中获取company存入session
		if request.GET.get('company'):
			request.session['company'] = request.GET.get('company')
		# 创建Context
		ctx = {'company'      : request.session['company'],
		       'accident_type': request.session['accident_type']}

		# 如果存在Claim ID
		if request.session.get('claim_id'):
			claim = Claim.objects.get(id=request.session.get('claim_id'))
			ctx['car_plate'] = claim.car_plate
			ctx['time'] = claim.time
			ctx['location'] = claim.location

		return render(request, 'claim_fill_claim.html', ctx)

	elif request.method == 'POST':
		if request.POST.get('car_plate') and \
				request.POST.get('time') and \
				request.POST.get('location'):
			company = InsuranceCompany.objects.get(name=request.session['company'])
			if request.session.get('claim_id'):
				claim = Claim.objects.get(id=request.session.get('claim_id'))
				claim.company_id = company.id
				claim.accident_type = request.session['accident_type']
				claim.car_plate = request.POST.get('car_plate')
				claim.time = request.POST.get('time')
				claim.location = request.POST.get('location')
				claim.save()
			else:
				new_claim = Claim.objects.create(
					user_id=request.session['user_id'],
					company_id=company.id,
					accident_type=request.session['accident_type'],
					car_plate=request.POST.get('car_plate'),
					time=request.POST.get('time'),
					location=request.POST.get('location'),
				)
				request.session['claim_id'] = new_claim.id

			request.session['img_upload_step'] = 1
			return HttpResponseRedirect('/claim/upload')


def claim_img_upload(request):
	user_id = request.session.get('user_id')
	company = request.session.get('company')
	accident_type = request.session.get('accident_type')
	claim_id = request.session.get('claim_id')

	# 重定向未登录用户
	if not user_id:
		return HttpResponseRedirect('/claim')

	# 重定向无type用户
	if not accident_type and not request.GET.get('accident_type'):
		return HttpResponseRedirect('/claim')

	# 重定向无company用户
	if not company and not request.GET.get('company'):
		return HttpResponseRedirect('/claim')

	# 重定向无claim_id用户
	if not claim_id and not request.GET.get('claim_id'):
		return HttpResponseRedirect('/claim')

	if request.GET.get('accident_type'):
		accident_type = request.GET.get('accident_type')

	if request.GET.get('company'):
		company = request.GET.get('company')

	if request.GET.get('claim_id'):
		claim_id = request.GET.get('claim_id')

	img_upload_step = request.session.get('img_upload_step', 1)

	type_step = {
		'danche' : ['站在事故车辆前45度角，10米处拍照。如下图：',
		            '站在事故车辆前45度角，5米处拍照。如下图：',
		            '站在事故车辆前45度角，1米处拍照。如下图：',
		            '站在事故车辆后45度角，10米处拍照。如下图：',
		            '站在事故车辆后45度角，5米处拍照。如下图：',
		            '站在事故车辆后45度角，1米处拍照。如下图：',
		            '在事故车辆前挡风玻璃处拍照车辆识别代号。如下图：',
		            '车辆移开后对准车辆受损部位和擦刮物体部位拍照。如下图：',
		            '人车合影，站在事故车辆前方或后方，拿手机对准自己和事故车辆拍照，必须照下事故车辆的号牌。如下图：',
		            '拿出行车证拍照。如下图：',
		            '拿出驾驶证拍照。如下图：',
		            '拿出被保险人身份证正面拍照。如下图：',
		            '拿出被保险人身份证反面拍照。如下图：',
		            '拿出被被保险人银行卡拍照。如下图：'
		            ],
		'guaca'  : ['站在事故车辆前45度角，10米处拍照。如下图：',
		            '站在事故车辆前45度角，5米处拍照。如下图：',
		            '站在事故车辆前45度角，1米处拍照。如下图：',
		            '站在事故车辆后45度角，10米处拍照。如下图：',
		            '站在事故车辆后45度角，5米处拍照。如下图：',
		            '站在事故车辆后45度角，1米处拍照。如下图：',
		            '在事故车辆前挡风玻璃处拍照车辆识别代号。如下图：',
		            '车辆移开后对准己方车辆受损部位和擦刮物体部位拍照。如下图：',
		            '车辆移开后对准对方车辆受损部位和擦刮物体部位拍照。如下图：',
		            '人车合影，站在事故车辆前方或后方，拿手机对准自己和事故车辆拍照，必须照下事故车辆的号牌。如下图：',
		            '拿出行车证拍照。如下图：',
		            '拿出驾驶证拍照。如下图：',
		            '拿出被保险人身份证正面拍照。如下图：',
		            '拿出被保险人身份证反面拍照。如下图：',
		            '拿出被被保险人银行卡拍照。如下图：'
		            ],
		'zhuiwei': ['站在事故车辆前45度角，10米处拍照。如下图：',
		            '站在事故车辆前45度角，5米处拍照。如下图：',
		            '站在事故车辆前45度角，1米处拍照。如下图：',
		            '站在事故车辆后45度角，10米处拍照。如下图：',
		            '站在事故车辆后45度角，5米处拍照。如下图：',
		            '站在事故车辆后45度角，1米处拍照。如下图：',
		            '在事故车辆前挡风玻璃处拍照车辆识别代号。如下图：',
		            '车辆移开后对准己方车辆受损部位和擦刮物体部位拍照。如下图：',
		            '车辆移开后对准对方车辆受损部位和擦刮物体部位拍照。如下图：',
		            '人车合影，站在事故车辆前方或后方，拿手机对准自己和事故车辆拍照，必须照下事故车辆的号牌。如下图：',
		            '拿出行车证拍照。如下图：',
		            '拿出驾驶证拍照。如下图：',
		            '拿出被保险人身份证正面拍照。如下图：',
		            '拿出被保险人身份证反面拍照。如下图：',
		            '拿出被被保险人银行卡拍照。如下图：'
		            ],
	}
	if request.method == 'GET':
		# Perform Back
		if request.GET.get('back'):
			if img_upload_step == 1:
				return HttpResponseRedirect('/claim/fill')
			else:
				img_upload_step -= 1
				request.session['img_upload_step'] = img_upload_step
				step_name = type_step[accident_type][img_upload_step - 1]
				# Demo img url
				img_url = 'img/' + accident_type + '/' + str(img_upload_step - 1) + '.png'

				return render(request, 'claim_img_upload.html', {'type'     : accident_type,
				                                                 'step'     : img_upload_step,
				                                                 'step_name': step_name,
				                                                 'img_url'  : img_url})

		# Create context
		step_name = type_step[accident_type][img_upload_step - 1]
		# Demo img url
		img_url = 'img/' + accident_type + '/' + str(img_upload_step - 1) + '.png'
		ctx = {'type'     : accident_type,
		       'step'     : img_upload_step,
		       'step_name': step_name,
		       'img_url'  : img_url}

		if request.GET.get('empty'):
			ctx['error_msg'] = '图片不得为空'

		return render(request, 'claim_img_upload.html', ctx)

	if request.method == 'POST':
		# 如果到了最后一步，跳转到结束页面
		if accident_type == 'danche' and img_upload_step == 14:
			return HttpResponseRedirect('/claim/finish')
		elif img_upload_step == 15:
			return HttpResponseRedirect('/claim/finish')

		if request.FILES.get('claim_img'):
			image, created = Image.objects.get_or_create(claim_id=claim_id, step=request.session['img_upload_step'])
			image.image = request.FILES.get('claim_img')
			image.save()
			img_upload_step += 1
			request.session['img_upload_step'] = img_upload_step

			return HttpResponseRedirect('/claim/upload')
		else:
			return HttpResponseRedirect('/claim/upload?empty=true')


def claim_finish(request):
	return render(request, 'claim_finish.html')
