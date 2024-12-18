from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import Member

# Register your models here.
class MemberAdmin(UserAdmin):
    model = Member
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']
    list_filter = ['is_staff', 'is_active']
    search_fields = ['username', 'email']
    ordering = ['username']

admin.site.register(Member, MemberAdmin)