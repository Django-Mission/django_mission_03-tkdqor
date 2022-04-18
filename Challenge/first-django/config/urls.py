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
from support.views import inquiry
from django.conf import settings    # 이미지 파일 업로드를 위한 settings import
from django.conf.urls.static import static  # 이미지 파일 업로드를 위한 static import

urlpatterns = [
    # admin 페이지 URL
    path('admin/', admin.site.urls),
    # 로또 게임 수 입력 페이지 URL
    path('lotto/', views.lotto, name='lotto'),
    # 로또 번호 추출기 결과 페이지 URL
    path('lotto/result/', views.result, name='result'),

    # 2차 Challenge 미션 URL
    path('inquiry/', inquiry, name='inquiry'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 이미지 serving를 위해 settings에서 설정한 MEDIA_URL로 요청이 들어올 경우, MEDIA_ROOT 내부에서 검색 후 HTTP Response로 응답
