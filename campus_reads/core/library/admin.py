from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', "semester") 

# Register your models here.
admin.site.register(Book, BookAdmin)