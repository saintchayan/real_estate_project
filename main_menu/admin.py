from django.contrib import admin
from .models import Picture, RentSale, ClientRequest


class PictureInline(admin.StackedInline):
    model = Picture


@admin.register(RentSale)
class SiteAdmin(admin.ModelAdmin):
    #     # list_display = ['city', 'type', 'district', 'address', 'owner', 'phone_number', 'price_in_lira']
    #     # ordering = ['district']
    #     # list_per_page = 10
    inlines = [PictureInline]
    pass


@admin.register(Picture)
class SiteAdmin(admin.ModelAdmin):
    #     # list_display = ['image']
    #     list_per_page = 100
    pass


@admin.register(ClientRequest)
class SiteAdmin(admin.ModelAdmin):
    pass
