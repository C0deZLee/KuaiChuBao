# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponseRedirect

# from .forms import ImageForm, PostForm
# from django.forms import modelformset_factory

from ..claim.models import UserInfo


def insure_landing(request):
	# formset = ImageFormSet(queryset=Images.objects.none())
	if not request.session.get('company', False):
		return HttpResponseRedirect('/claim/company')
	if request.session.get('type', False) and request.session.get('step', False):
		return HttpResponseRedirect('/claim/upload')
	elif request.session.get('type', False):
		return HttpResponseRedirect('/claim/user')
	else:
		return render(request, 'landing.html')


def insurance_company(request):
	if request.method == 'GET':
		return render(request, 'insuranceCompany.html')
	elif request.method == 'POST':
		pass


def user_register(request):
	if request.method == 'GET':
		if request.GET.get('type', False):
			request.session['type'] = request.GET.get('type')
			return render(request, 'userRegister.html')
		elif request.session.get('type', False):
			request.session['type'] = request.GET.get('type')
			return render(request, 'userRegister.html')
		else:
			return render(request, '404.html')

	elif request.method == 'POST':
		if request.POST.get('name', False) and request.POST.get('national_id', False) and request.POST.get('phone', False) and request.POST.get('car_plate', False):
			user, create = UserInfo.objects.get_or_create(
				national_id_number=request.POST.get('national_id'),
			)
			user.name = request.POST.get('name')
			user.phone = request.POST.get('phone')
			user.car_plate = request.POST.get('car_plate')
			user.save()
			request.session['step'] = 1
			request.session['user_id'] = user.id
			return HttpResponseRedirect('/upload')


def image_upload(request):
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
		            '拿出被保险人身份证拍照。如下图：',
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
		            '拿出被保险人身份证拍照。如下图：',
		            '拿出被被保险人银行卡拍照。如下图：'
		            ],
	}

	if request.session.get('type', False) and request.session.get('step', False):
		type = request.session.get('type', False)
		step = request.session.get('step', False)
		step_name = type_step[type][step - 1]
		img_url = 'img/' + type + '/' + str(step) + '.png'

		return render(request, 'imageUpload.html', {'type'     : type,
		                                            'step'     : step,
		                                            'step_name': step_name,
		                                            'img_url'  : img_url})

#
# def post_picture(request):
# 	ImageFormSet = modelformset_factory(Images,
# 	                                    form=ImageForm, extra=3)
#
# 	if request.method == 'POST':
#
# 		postForm = PostForm(request.POST)
# 		formset = ImageFormSet(request.POST, request.FILES,
# 		                       queryset=Images.objects.none())
#
# 		if postForm.is_valid() and formset.is_valid():
#
# 			# add a new claim and link the posted form with claim
# 			post_form = postForm.save(commit=False)
# 			post_form.save()
#
# 			for form in formset.cleaned_data:
# 				# try:
# 				image = form['image']
# 				photo = Images(image=image)
# 				photo.save()
# 			# except:
# 			#    pass
# 			# messages.success(request,
# 			#                 "Yeeew,check it out on the home page!")
# 			return HttpResponseRedirect("/")
# 		else:
# 			print postForm.errors, formset.errors
# 	else:
# 		postForm = PostForm()
# 		formset = ImageFormSet(queryset=Images.objects.none())
# 	return render(request, 'index.html', {'postForm': postForm, 'formset': formset})
