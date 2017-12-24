"""KuaiChuBao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.shortcuts import render

from KuaiChuBao.modules.claim import urls as claim_urls
from KuaiChuBao.modules.insure import urls as insure_urls


def Error404(request):
	return render(request, '404.html')


urlpatterns = [
	url(r'^claim/', include(claim_urls)),
	url(r'^insure/', include(insure_urls)),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^404/', Error404),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

