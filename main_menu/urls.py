from django.urls import path
from .views import *
from .serializer import RentSaleSerializer

urlpatterns = [
    path('', Menu.as_view(), name='all_objects'),
    path('contacts/', contacts, name='contacts'),
    path('sale/', Sale.as_view(), name='sale_list'),
    path('rent/', Rent.as_view(), name='rent_list'),
    path('about_us/', about_us, name='about_us'),
    path('medical_insurance/', medical_insurance, name='medical_insurance'),
    path('resident_card/', resident_card, name='resident_card'),
    path('detail/<int:pk>', ObjectDetail.as_view(), name='detail_view'),
]