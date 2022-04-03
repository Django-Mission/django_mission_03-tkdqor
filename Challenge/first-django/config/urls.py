"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from demos import views

urlpatterns = [
    # admin 페이지 URL
    path('admin/', admin.site.urls),
    # 로또 게임 수 입력 페이지 URL
    path('lotto/', views.lotto, name='lotto'),
    # 로또 번호 추출기 결과 페이지 URL
    path('lotto/result/', views.result, name='result'),
]
