from django.urls import path
from . import views

app_name = 'beneficiario'
urlpatterns = [
    path('', views.buscar, name='buscar'),
    path('detail/', views.detail, name='detail'),
    path('list/', views.list, name='list'),
]