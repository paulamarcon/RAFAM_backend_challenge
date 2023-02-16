from django.contrib import admin
from friends_lessons.models import User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["firstname"]


