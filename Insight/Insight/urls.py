"""Insight URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='API')
from django.contrib.auth import views as auth_views
logout_template_name = {'template_name': 'rest_framework/logout.html'}
login_template_name = {'template_name': 'rest_framework/login.html'}

urlpatterns = [
    url(r'^api/'    , include('api.urls', namespace='api')),
    url(r'^admin/'  , admin.site.urls),
    url(r'^login/$' , auth_views.login, login_template_name, name='login') ,
    url(r'^logout/$', auth_views.logout,logout_template_name, name='logout'),
]
