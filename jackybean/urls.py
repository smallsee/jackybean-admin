# -*- coding: utf-8 -*-
"""jackybean URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
# from django.contrib import admin
import xadmin
from jackybean.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from article.views import ArticleListViewSet

router = DefaultRouter()

#配置article的url
router.register(r'article', ArticleListViewSet, base_name="article")

urlpatterns = [
   url(r'^xadmin/', xadmin.site.urls),
   url(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),

   # drf自带的认证模式
   url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
   url(r'^api-token-auth/', views.obtain_auth_token),

   url(r'^', include(router.urls)),

   url(r'docs/', include_docs_urls(title="魔豆启城")),
]
