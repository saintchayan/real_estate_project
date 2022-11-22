from django.forms import model_to_dict
from django.http import HttpResponse
from django.template.loader import render_to_string
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import RentSale
from django.views.generic import ListView, DetailView
from rest_framework import generics
from main_menu.serializer import RentSaleSerializer


class RentSalesAPIView(APIView):
    def get(self, request):
        list_of_objects = RentSale.objects.all()
        return Response({'posts': RentSaleSerializer(list_of_objects, many=True).data})

    def post(self, request):
        serializer = RentSaleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        new_object = RentSale.objects.create(
            type = request.data['type'],
            city = request.data['city'],
            district = request.data['district'],
            address = request.data['address'],
            owner = request.data['owner'],
            phone_number = request.data['phone_number'],
            price_in_lira = request.data['price_in_lira'],
            created_data = request.data['created_data'],
            updated_time = request.data['updated_time'],
            description = request.data['description']
        )
        return Response({'post': RentSaleSerializer(new_object).data})


# class RentSalesAPIView(generics.ListAPIView):
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

# def sale(request):
#     response = render_to_string('main_menu/sale.html')
#     return HttpResponse(response)

# def rent(request):
#     response = render_to_string('main_menu/rent.html')
#     return HttpResponse(response)

# def menu(request):
#     flats = RentSale.objects.all()
#     return render(request, 'main_menu/menu.html', {'flats': flats})
