# pages/urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
    url('about/', views.AboutPageView.as_view(), name='about'),
    url('', views.HomePageView.as_view(), name='home'),
]