"""ApiTest URL Configuration

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
from django.contrib import admin
from django.conf.urls import url

from MyApp.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^welcome/$', welcome), #进入主页
    url(r'home/$', home), #进入首页
    url(r"^child/(?P<eid>.+)/(?P<oid>.*)/$", child), #返回子页面
    url(r'login/$', login), #进入登录页面
]
