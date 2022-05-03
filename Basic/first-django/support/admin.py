from django.contrib import admin
from .models import Faq, Inquiry, Answer


# 어드민 페이지에서 Inquiry 모델 조회 시, Answer 모델을 같이 볼 수 있게 AnswerInline 클래스 설정
class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1
    min_num = 3
    max_num = 5
    verbose_name = '댓글'
    verbose_name_plural = '댓글'


# Faq 모델 등록
@admin.register(Faq)
class FaqModelAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'updated_at')
    search_fields = ('question', )
    list_filter = ('category', )
    search_help_text = '질문 제목 검색이 가능합니다.'
    readonly_fields = ('created_at', 'updated_at')


# Inquiry 모델 등록
@admin.register(Inquiry)
class InquiryModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'writer')
    search_fields = ('title', 'email', 'phonenumber')
    list_filter = ('category', )
    search_help_text = '질문 제목과 이메일, 핸드폰 번호 검색이 가능합니다.'
    readonly_fields = ('created_at', 'updated_at')
    inlines = [AnswerInline]

