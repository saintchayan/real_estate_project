from django.forms import model_to_dict
from django.http import HttpResponse
from django.template.loader import render_to_string
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import RentSale
from django.views.generic import ListView, DetailView
from rest_framework import generics
from main_menu.serializer import RentSaleSerializer


class RentSalesAPIList(generics.ListCreateAPIView):
    queryset = RentSale.objects.all()
    serializer_class = RentSaleSerializer


class RentSalesAPIView(APIView):
    def get(self, request):
        list_of_objects = RentSale.objects.all()
        return Response({'posts': RentSaleSerializer(list_of_objects, many=True).data})

    def post(self, request):
        serializer = RentSaleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"Error": "Method PUT not allowed"})

        try:
            instance = RentSale.objects.get(pk=pk)
        except:
            return Response({"Error": "Object does not exist"})

        serializer = RentSaleSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    # def delete(self, request, *args, **kwargs):
    #     pk = kwargs.get("pk", None)
    #     if not pk:
    #         return Response({"Error": "Method DELETE not allowed"})
    #
    #     return Response({"post": "delete post " + str(pk)})


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
