from django.db import models
from django.contrib.auth import get_user_model           # User 모델 가져오기 위해 import
from django.utils.translation import gettext_lazy as _   # 해당 함수로 문자열을 정의해서 다국어 처리 가능


# get_user_model 함수를 이용해서 User 모델 가져오기 / 나중에 User 모델을 쉽게 커스텀하기 위함
User = get_user_model()


class Faq(models.Model):

    class Category(models.TextChoices):        # 카테고리 종류를 클래스로 정의
        NORMAL = 'NORMAL', _('일반')
        ACCOUNT = 'ACCOUNT', _('계정')
        ETC = 'ETC', _('기타')
    
    question = models.CharField(max_length=200, null=False, blank=False)
    category = models.CharField(max_length=10, choices=Category.choices, default=Category.NORMAL)
    answer = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='writer_faq')
    created_at = models.DateTimeField(auto_now_add=True)
    editor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='editor_faq')
    updated_at = models.DateTimeField(auto_now=True)



    
