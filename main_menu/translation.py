from modeltranslation.translator import register, TranslationOptions
from .models import RentSale, ClientRequest


@register(RentSale)
class RentSaleTranslationOption(TranslationOptions):
    fields = ('description',)
