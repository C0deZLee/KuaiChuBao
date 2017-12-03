from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.insure_landing, name='claim_landing'),
]