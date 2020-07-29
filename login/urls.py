from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^in$', views.login_view, name='login_view'),
    url(r'^out$', views.logout_view, name='logout_view'),
    url(r'^home$', views.home, name='home')
]