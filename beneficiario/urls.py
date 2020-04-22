from django.urls import path
from . import views

app_name = 'beneficiario'
urlpatterns = [
    path('', views.beneficiario_buscar, name='beneficiario_buscar'),
    path('beneficiario/detail/', views.beneficiario_detail, name='beneficiario_detail'),
    path('beneficiario/advertencia', views.beneficiario_advertencia, name='beneficiario_advertencia'),
    path('list/', views.list, name='list'),
]