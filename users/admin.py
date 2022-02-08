from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from board.views import kanban
from .models import *

# Register your models here.
admin.site.register(CustomUser, UserAdmin)

