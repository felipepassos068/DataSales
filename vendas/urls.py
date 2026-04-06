from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='home/', permanent=True)),

    path('home/', views.home, name='home'),
    path('registrar/', views.register, name='register'),
    path('consultar/', views.consult, name='consult'),
    path('relatorio/', views.relatorio, name='relatorio')
]