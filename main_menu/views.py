from django.forms import model_to_dict
from django.http import HttpResponse
from django.template.loader import render_to_string
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import RentSale
from django.views.generic import ListView, DetailView
from rest_framework import generics, viewsets, mixins
from main_menu.serializer import RentSaleSerializer


class RentSalesViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = RentSale.objects.all()
    serializer_class = RentSaleSerializer


# class RentSalesAPIList(generics.ListCreateAPIView):
#     queryset = RentSale.objects.all()
#     serializer_class = RentSaleSerializer
#
#
# class RentSalesAPIUpdate(generics.UpdateAPIView):
#     queryset = RentSale.objects.all()
#     serializer_class = RentSaleSerializer
#
#
# class RentSalesAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = RentSale.objects.all()
#     serializer_class = RentSaleSerializer


class Menu(ListView):
    template_name = 'main_menu/menu.html'
    model = RentSale


class Sale(ListView):
    template_name = 'main_menu/sale.html'
    model = RentSale
    context_object_name = 'sales'


class Rent(ListView):
    template_name = 'main_menu/rent.html'
    model = RentSale
    context_object_name = 'rents'


class ObjectDetail(DetailView):
    template_name = 'main_menu/detail_view.html'
    model = RentSale


def contacts(request):
    response = render_to_string('main_menu/contacts.html')
    return HttpResponse(response)


def about_us(request):
    response = render_to_string('main_menu/about_us.html')
    return HttpResponse(response)


def medical_insurance(request):
    response = render_to_string('main_menu/medical_insurance.html')
    return HttpResponse(response)


def resident_card(request):
    response = render_to_string('main_menu/resident_card.html')
    return HttpResponse(response)
