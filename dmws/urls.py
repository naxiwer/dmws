"""dmws URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()
from login import views as homeviews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', include('login.urls')),
#    url(r'sql/', include('sqlonline.urls')),
#    url(r'rds/', include('rds.urls')),
#    url(r'redis/', include('redisadmin.urls')),
    url(r'^$', homeviews.index, name='index'),
    url(r'^home$', homeviews.home, name='home'),
    # url(r'^logout$', 'login.views.logout_view', name='logout'),
    # url(r'^login$','login.views.login_view', name='logcheck'),
    #     url(r'^checkbackup/', include('ckbackup.urls')),
    #     url(r'^datavis/', include('datavis.urls')),
]