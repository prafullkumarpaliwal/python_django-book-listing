from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Book, BookUser

# Register your models here.
admin.site.register(User)
admin.site.register(Book)
admin.site.register(BookUser)