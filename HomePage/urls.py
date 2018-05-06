# pages/urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^blog/(?P<pk>\d+)/$', views.BlogDetailView.as_view(), name='blog_detail'),
    url(r'^blog/$', views.BlogListView.as_view(), name='blog'),
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    url(r'^$', views.HomePageView.as_view(), name='home'),

]