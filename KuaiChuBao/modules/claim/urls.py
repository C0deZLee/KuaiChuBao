from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.claim_user, name='claim_user_login'),
	url(r'^new_or_resume$', views.claim_new_or_resume, name='claim_new_or_resume'),
	url(r'^resume', views.claim_resume, name='claim_resume'),

	url(r'^type$', views.claim_chose_accident_type, name='claim_chose_accident_type'),
	url(r'^company$', views.claim_chose_company, name='claim_chose_company'),
	url(r'^fill', views.claim_fill_claim, name='claim_fill_claim'),
	url(r'^upload$', views.claim_img_upload, name='claim_img_upload'),
	url(r'^finish$', views.claim_finish, name='claim_finish'),
]
