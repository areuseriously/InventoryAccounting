from django.contrib import admin
from django.contrib.auth.models import User
from .models import Department, Position, UserProfile
from django.contrib.auth.admin import UserAdmin

admin.site.register(Department)
admin.site.register(Position)
admin.site.register(UserProfile)


class UserInLine(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Accounts'


class CustomizedUserAdmin(UserAdmin):
    inlines = (UserInLine,)


admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)
