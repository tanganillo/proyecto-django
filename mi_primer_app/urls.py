from django.urls import path

from .views import saludo, saludo_con_template

urlpatterns = [
    path('hola-mundo/', saludo),
    path('hola-mundo-template/', saludo_con_template),
]