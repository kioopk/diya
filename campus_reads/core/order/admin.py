from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "books",)

# Register your models here.
admin.site.register(Order, OrderAdmin)