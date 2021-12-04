"""factura_ms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from app_factura.views import PlazaCreateView, PlazaDetailView, PlazaUpdateView, PlazaDeleteView, AvailablePlazas
from app_factura.views import FacturaCreateView, FacturaDetailView, FacturaUpdateView, FacturaDeleteView, CheckOutView 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('plaza/create/',          PlazaCreateView.as_view()),
    path('plaza/<int:pk>/',        PlazaDetailView.as_view()),
    path('plaza/update/<int:pk>/', PlazaUpdateView.as_view()),
    path('plaza/delete/<int:pk>/', PlazaDeleteView.as_view()),
    path('plaza/available/',       AvailablePlazas.as_view()),

    path('factura/create/',          FacturaCreateView.as_view()),
    path('factura/<int:pk>/',        FacturaDetailView.as_view()),
    path('factura/update/<int:pk>/', FacturaUpdateView.as_view()),
    path('factura/delete/<int:pk>/', FacturaDeleteView.as_view()),
    path('factura/checkout/<int:pk>/', CheckOutView.as_view()),
]
