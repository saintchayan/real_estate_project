from django.urls import path
from .views import *

urlpatterns = [
    path('', Menu.as_view()),
    path('contacts/', contacts),
    path('sale/', Sale.as_view()),
    path('rent/', Rent.as_view()),
    path('about_us/', about_us),
    path('medical_insurance/', medical_insurance),
    path('resident_card/', resident_card),
]