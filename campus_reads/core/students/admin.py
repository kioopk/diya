from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser

class UserAdmin(BaseUserAdmin):
    ordering = ['enrollmentno']
    list_display = ['enrollmentno', 'fullname', 'is_staff']
    
    fieldsets = (
        (None, {'fields': ('enrollmentno', 'password')}),
        (_('Personal info'), {'fields': ('fullname',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('enrollmentno', 'fullname', 'password1', 'password2'),
        }),
    )

admin.site.register(CustomUser, UserAdmin)

