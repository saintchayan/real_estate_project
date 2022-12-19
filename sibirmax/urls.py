from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from main_menu.views import *


admin.site.site_header = 'SIBIRMAX'
admin.site.index_title = 'Satilik'

router = routers.DefaultRouter()
router.register(r'object_list', RentSalesViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_menu.urls')),
    path('api/v1/', include(router.urls)),
    # path('api/v1/object_list/', RentSalesAPIList.as_view()),
    # path('api/v1/object_list/<int:pk>/', RentSalesAPIUpdate.as_view()),
    # path('api/v1/object_detail/<int:pk>/', RentSalesAPIDetailView.as_view()),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)