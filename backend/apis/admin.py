from django.contrib import admin
from .models import *

class CustomAdmin(admin.ModelAdmin):
    list_display = ['email' , 'get_usertype' , 'password']

admin.site.register(CustomUser,CustomAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ['Name' , "Author"]
admin.site.register(Book,BookAdmin)

