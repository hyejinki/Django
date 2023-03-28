from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = ("username", "nickname")
    add_fieldsets = (
        (
        None,
        {
            "classes" : ("wide",), 
            "fields" : ("username", "password1", "password2",  "nickname", )
        },
        )
    )   

# Register your models here.
admin.site.register(User, UserAdmin)