from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Profile

class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name','type',
        )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)
