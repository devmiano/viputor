from api.models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


class UserProfileAdmin(UserAdmin):
    ordering = ['email', ]

    readonly_fields = ('last_login', 'joined')

    list_display = ('name', 'email', 'contact', 'is_patron',
                    'is_user', 'is_staff', 'is_superuser',)
    search_fields = ('name', 'contact', 'email')

    list_filter = [
        'is_staff', 'is_superuser', 'is_patron', 'is_user', 'is_moderator',
    ]

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            'Personal info',
            {
                'fields': (
                    'name',
                    'contact',
                )
            },
        ),
        (
            'Location info',
            {
                'fields': (
                    'city',
                    'address',
                    'location',
                )
            },
        ),
        (
            'Timeline',
            {
                'fields': (
                    'joined',
                    'last_login',
                )
            },
        ),
        (
            'Permissions',
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_user',
                    'is_patron',
                    'is_moderator',
                    'is_superuser',
                )
            },
        ),
        (
            'Advanced options',
            {
                'classes': ('collapse',),
                'fields': (
                    'groups',
                    'user_permissions',
                )
            },
        ),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide', 'extrapretty'),
            'fields': ('name', 'email', 'contact', 'is_user',
                       'is_patron', 'is_moderator', 'password1', 'password2'),
        }),
    )


admin.site.register(UserProfile, UserProfileAdmin)
