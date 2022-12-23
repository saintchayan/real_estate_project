from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic.edit import FormView
from rest_framework.viewsets import GenericViewSet
from .forms import ClientRequestForm
from .models import RentSale
from django.views.generic import ListView, DetailView
from rest_framework import mixins
from main_menu.serializer import RentSaleSerializer


class RentSalesViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = RentSale.objects.all()
    serializer_class = RentSaleSerializer


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


class ClientRequestView(FormView):
    form_class = ClientRequestForm
    template_name = 'main_menu/client_request.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super(ClientRequestView, self).form_valid(form)


def contacts(request):
    return render(request, 'main_menu/contacts.html')


def about_us(request):
    return render(request, 'main_menu/about_us.html')


def medical_insurance(request):
    return render(request, 'main_menu/medical_insurance.html')


def resident_card(request):
    return render(request, 'main_menu/resident_card.html')


def terms_of_use(request):
    return render(request, 'main_menu/terms_of_use.html')


def privacy_policy(request):
    return render(request, 'main_menu/privacy_policy.html')


def frequently_asked_questions(request):
    return render(request, 'main_menu/frequently_asked_questions.html')


def citizenship(request):
    return render(request, 'main_menu/citizenship.html')
