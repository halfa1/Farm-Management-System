from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    #model to map
    model = CustomUser
    #this maps to the list of users shown
    list_display = ("username","email","is_staff","is_active","date_joined")
    list_filter = ("is_staff","is_active")

    #search filter
    search_fields = ("username","email")
    #list ordering
    ordering = ("username",)

    #create superuser ie first admin
   # python manage.py createsuperuser
   #enter password