"""
URL configuration for MedicalShopManagementSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name="home"),
    path('<int:id>/dealer_delete/',views.dealer_delete,name="dealer_delete"),
    path('<int:id>/dealer_update',views.dealer_update,name="dealer_update"),
    path('<int:id>/medicine_delete/',views.medicine_delete,name="medicine_delete"),
    path('<int:id>/medicine_update',views.medicine_update,name="medicine_update"),
    path('<int:id>/employee_delete/',views.employee_delete,name="employee_delete"),
    path('<int:id>/employee_update',views.employee_update,name="employee_update"),
    path('<int:id>/customer_delete/',views.customer_delete,name="customer_delete"),
    path('<int:id>/customer_update',views.customer_update,name="customer_update"),
    path('<int:id>/purchase_delete/',views.purchase_delete,name="purchase_delete"),
    path('<int:id>/purchase_update',views.purchase_update,name="purchase_update"),
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)