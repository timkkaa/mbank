from django.contrib import admin

from journal.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'phone_number', 'balance']
