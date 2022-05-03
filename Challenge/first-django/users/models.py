from django.db import models
from django.contrib.auth.models import AbstractUser  # User 모델을 커스텀하기 위해 import


# 기존 사용자 모델인 User 커스텀
class User(AbstractUser):
    phone = models.CharField(verbose_name='전화번호', max_length=13)   # 기존 사용자 모델 User에 phone 필드 추가
