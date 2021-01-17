from django.contrib import admin
from django.contrib.admin import ModelAdmin

from authentication.models import User, UserDetails


# Register your models here.
@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = ["id", "username", "first_name", "last_name", "email", "role", "relation"]
    list_filter = ["id", "username", "role"]


admin.site.register(UserDetails)