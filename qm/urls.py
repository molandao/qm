"""qm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from users import views
from users.views import LoginView, RegisterView,ActiveUserView,ForgetPwdView,ResetView,ModifyPwdView
from organization.views import OrgView
from django.urls import include

from django.views.static import serve
from qm.settings import MEDIA_ROOT
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    # not transfer function,just direct this fun
    path('',views.home, name = 'index'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/',RegisterView.as_view(),name='register'),
    path('captcha/',include('captcha.urls')),
    path('active/<active_code>/',ActiveUserView.as_view(),name='user_active'),
    path('forget/',ForgetPwdView.as_view(),name='forget_pwd'),
    path('reset/<active_code>/', ResetView.as_view(), name='reset_pwd'),
    path('modify_pwd/', ModifyPwdView.as_view(), name='modify_pwd'),

    path('org/', include('organization.urls')),

    path('articles/', include('articles.urls', namespace="articles")),
    # 配置上传文件的访问处理函数
    path('media/<path>', serve, {"document_root":MEDIA_ROOT}),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
