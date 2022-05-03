from django.contrib import admin
from .models import Inquiry, Answer


# 어드민 페이지에서 Answer 모델을 Inquiry 모델과 같이 볼 수 있게 AnswerInline 클래스 설정
class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1
    min_num = 1
    max_num = 5
    verbose_name = '답변'
    verbose_name_plural = '답변'


@admin.register(Inquiry)
class InquiryModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'state', 'created_at', 'writer')
    search_fields = ('title', 'email', 'phonenumber', 'writer__username', 'writer__email', 'writer__phone') 
    # User 모델의 username / email / phone 필드로 검색
    list_filter = ('category', 'state')
    readonly_fields = ('created_at', 'updated_at')
    search_help_text = '질문 제목과 이메일, 핸드폰 번호로 검색이 가능합니다.'
    inlines = [AnswerInline]

    # 액션 추가하기
    actions = ['send_response']

    def send_response(modeladmin, request, queryset):
        for item in queryset:
            if item.is_email and item.is_phone == True:
                print(item.email, item.phonenumber, sep='\n')
                


