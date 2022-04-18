from django.contrib import admin
from .models import Inquiry, Answer

# Register your models here.

@admin.register(Inquiry)
class InquiryModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'content', 'phonenumber', 'writer', 'created_at', 'updated_at')

@admin.register(Answer)
class AnswerModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'inquiry', 'content', 'writer', 'created_at', 'editor', 'updated_at')