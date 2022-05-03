from django.db import models
from django.contrib.auth import get_user_model           # User 모델 가져오기 위해 import
from django.utils.translation import gettext_lazy as _   # 해당 함수로 문자열을 정의해서 다국어 처리 가능
from django.core.validators import RegexValidator        # 입력된 핸드폰번호 유효성 검증을 위해 import


# get_user_model 함수를 이용해서 User 모델 가져오기 / 나중에 User 모델을 쉽게 커스텀하기 위함
User = get_user_model()


# 1:1문의 모델
class Inquiry(models.Model):

    class Category(models.TextChoices):        # 카테고리 종류를 클래스로 정의
        ORDER = 'ORDER', _('주문')
        PAYMENT = 'PAYMENT', _('결제')
        DELIVERY = 'DELIVERY', _('배송')
        REFUND = 'REFUND', _('환불')
        ACCOUNT = 'ACCOUNT', _('계정')
        ETC = 'ETC', _('기타')
    
    class State(models.TextChoices):
        REGISTER = 'REGISTER', _('문의 등록')
        RECEIPT = 'RECEIPT', _('접수 완료')
        ANSWER = 'ANSWER', _('답변 완료')

    title = models.CharField(verbose_name="질문 제목", max_length=200)
    category = models.CharField(verbose_name="카테고리", max_length=10, choices=Category.choices, default=Category.ETC)
    state = models.CharField(verbose_name="상태", max_length=10, choices=State.choices, default=State.REGISTER)
    email = models.EmailField(max_length=50)
    is_email = models.BooleanField(verbose_name='이메일 수신 여부', default=False)
    phoneNumberRegex = RegexValidator(regex = r'^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$')  # 핸드폰번호 유효성 판단을 위한 정규식 코드
    phonenumber = models.CharField(validators = [phoneNumberRegex], max_length = 14)              # 정규식 코드를 이용해서 핸드폰번호 저장 
    is_phone = models.BooleanField(verbose_name='문자메시지 수신 여부', default=False)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='support/inquiry/%Y/%m/%d')
    writer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="생성자")
    created_at = models.DateTimeField(verbose_name="생성 일시", auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# 답변 모델
class Answer(models.Model):
    inquiry = models.ForeignKey(Inquiry, on_delete=models.CASCADE, related_name='inquiry_answer')
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='writer_answer')
    created_at = models.DateTimeField(auto_now_add=True)
    editor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='editor_answer')
    updated_at = models.DateTimeField(auto_now=True)