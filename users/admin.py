from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active', 'first_name',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None,
            {'fields': (
             ('first_name', 'last_name'),
             'street_address',
             'address2',
             'city',
             'state',
             'email',
             'password',

             )}
         ),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', 'extrapretty'),
            'fields': (('first_name', 'last_name'), 'email', ('password1', 'password2'), 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
