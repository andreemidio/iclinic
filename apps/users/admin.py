# Register your models here.
from django.contrib import admin

from apps.users.models import Users


@admin.register(Users)
class UsersProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'cellphone', 'email', 'created_at', 'is_active')
    search_fields = ('id', 'fullname', 'cellphone', 'email', 'created_at', 'is_active')
