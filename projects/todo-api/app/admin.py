from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


# class CustomUserAdmin(UserAdmin):
#     model = User
#
#     search_fields = ('email',)
#     ordering = ('email',)
#
#
# admin.site.register(User, CustomUserAdmin)
