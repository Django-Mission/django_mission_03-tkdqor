from django.contrib import admin
from .models import User, Userinfo

# Register your models here.

@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Userinfo)
class UserModelAdmin(admin.ModelAdmin):
    pass