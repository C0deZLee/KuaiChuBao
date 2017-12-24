from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.insure_user, name='insure_user_login'),
]