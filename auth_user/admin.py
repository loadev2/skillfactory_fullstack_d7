from django.contrib import admin
from auth_user.models import UserProfile

# Register your models here.
@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    pass