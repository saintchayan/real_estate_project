from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import RentSale
from django.views.generic import ListView, DetailView


# Create your views here.
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
