from django.contrib import admin
from .models import*

# Register your models here.
class signupdata(admin.ModelAdmin):
    list_display=['firstname','lastname','mobile','username','password']

admin.site.register(usersignup,signupdata)

admin.site.register(mynotes)

admin.site.register(contactus)