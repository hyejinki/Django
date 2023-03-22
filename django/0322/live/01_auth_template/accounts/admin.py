from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
class userAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, userAdmin)