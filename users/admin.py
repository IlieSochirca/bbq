from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import AccountCreationForm, AccountChangeForm
from .models import User


class UserAdmin(BaseUserAdmin):
    """
    Inform Admin Panel about the Custom User Model
    """
    add_form = AccountCreationForm
    form = AccountChangeForm
    model = User
    list_display = ('email', 'is_staff', 'is_active', 'profession', 'department',)
    list_filter = ('email', 'is_staff', 'is_active', 'profession', 'department',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name', 'profession', 'department',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'profession', 'department', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, UserAdmin)
