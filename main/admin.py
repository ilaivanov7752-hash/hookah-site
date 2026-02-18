from django.contrib import admin
from .models import Price

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ['item_name', 'price']
    list_editable = ['price']
    search_fields = ['item_name']