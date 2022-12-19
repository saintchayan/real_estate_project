from django.http import HttpResponse
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


def terms_of_use(request):
    response = render_to_string('main_menu/terms_of_use.html')
    return HttpResponse(response)


def privacy_policy(request):
    response = render_to_string('main_menu/privacy_policy.html')
    return HttpResponse(response)


def frequently_asked_questions(request):
    response = render_to_string('main_menu/frequently_asked_questions.html')
    return HttpResponse(response)
