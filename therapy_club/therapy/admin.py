from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from therapy.models import *

User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    pass
