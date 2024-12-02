from django.contrib import admin
from accounts.models import Profile
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','is_email_verified','email_token','profile_image']


admin.site.register(Profile, ProfileAdmin)