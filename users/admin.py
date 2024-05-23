from django.contrib import admin
from .models import CustomUser


# class CustomUserAdmin(admin.ModelAdmin):
    # list_display = ('id', 'username', 'is_staff', 'is_active', 'date_joined')
    # list_filter = ['id', 'username', 'is_staff', 'is_active', 'first_name']


# admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomUser)