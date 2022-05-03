from django.urls import path
from .views import signup_view, login_view

app_name = 'accounts'

urlpatterns = [
    # 회원가입 페이지 URL
    path('signup/', signup_view, name='signup'),
    # 로그인 페이지 URL
    path('login/', login_view, name='login'),
]