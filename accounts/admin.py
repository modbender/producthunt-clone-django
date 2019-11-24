from django.contrib import admin
from .models import UserInput

@admin.register(UserInput)
class UserInputAdmin(admin.ModelAdmin):
    pass
