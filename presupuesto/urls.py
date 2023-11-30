"""
URL configuration for escalaveinte project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.project_list,name="list"),
    path('presupuesto/<slug:slug_presupuesto>',views.project_detail, name="detail"),
    path('crear-presupuesto/', views.crear_presupuesto, name="crear_presupuesto"),
    path('eliminar-producto/<slug:slug_presupuesto>/<int:producto_id>/', views.eliminiar_producto, name='eliminar_producto'),
    path('elegir/',views.elegir, name="elegir"),
    path('crear-cliente/',views.crear_cliente, name="crear_cliente"),
    path('iniciar-sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('crear-pdf/<slug:slug_presupuesto>', views.crear_presupuesto_pdf, name='crearpdf'),

]