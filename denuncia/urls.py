from django.urls import path
from . import views

app_name = 'denuncia'
urlpatterns = [
    path('', views.denuncia_list, name='denuncia_list'),
    path('denuncia/<int:pk>/', views.denuncia_detail, name='denuncia_detail'),
    path('denuncia/nuevo', views.denuncia_nuevo, name='denuncia_nuevo'),
    path('denuncia/<int:pk>/edit/', views.denuncia_edit, name='denuncia_edit'),
]