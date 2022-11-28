from django.contrib import admin
from .models import RentSale


@admin.register(RentSale)
class SiteAdmin(admin.ModelAdmin):
    list_display = ['city', 'type', 'district', 'address', 'owner', 'phone_number', 'price_in_lira', 'image']
    ordering = ['district']
    list_per_page = 10