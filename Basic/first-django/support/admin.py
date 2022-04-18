from django.contrib import admin
from .models import Faq

# Faq 모델 등록
@admin.register(Faq)
class FaqModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'category', 'writer', 'created_at', 'editor', 'updated_at')
