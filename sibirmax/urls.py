"""sibirmax URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main_menu.views import *


admin.site.site_header = 'SIBIRMAX'
admin.site.index_title = 'Satilik'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_menu.urls')),
    path('api/v1/object_list/', RentSalesAPIList.as_view()),
    path('api/v1/object_list/<int:pk>/', RentSalesAPIList.as_view()),
]

# sudo fuser -k 8000/tcp - how to kill a process
