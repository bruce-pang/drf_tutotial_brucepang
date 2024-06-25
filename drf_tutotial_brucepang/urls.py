"""
URL configuration for drf_tutotial_brucepang project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views # 提供token认证的视图
from rest_framework.schemas import get_schema_view # 视图概要(类似于swagger)
from rest_framework.documentation import include_docs_urls # 文档

# schema_view = get_schema_view(title="DRF API文档", description="DRF API文档", version="1.0.0")

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token), # 获取token的接口
    path('api-auth/', include('rest_framework.urls')), # DRF的登录退出
    path('admin/', admin.site.urls),
    path('course/', include('course.urls')), # course的路由
   # path('schema/', schema_view), # schema视图(相当于swagger)
    path('docs/', include_docs_urls(title="DRF API文档", description="DRF API文档")), # 文档
]