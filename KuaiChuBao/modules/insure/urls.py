from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.insure_user, name='insure_user_login'),
	url(r'^company$', views.insure_company, name='insure_user_company'),
	url(r'^new_or_resume', views.insure_new_or_resume, name='insure_new_or_resume'),
	url(r'^past', views.insure_resume, name='insure_resume'),
	url(r'^form$', views.insure_form, name='insure_user_form'),
	url(r'^upload$', views.insure_upload, name='insure_user_upload'),
	url(r'^finish$', views.insure_complete, name='insure_user_complete'),
]
