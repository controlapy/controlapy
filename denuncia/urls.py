from django.urls import path, include
from . import views

app_name = 'denuncia'
urlpatterns = [
    path('', views.denuncia_list, name='denuncia_list'),
    path('denuncia/<int:pk>/', views.denuncia_detail, name='denuncia_detail'),
    path('denuncia/new/', views.denuncia_new, name='denuncia_new'),
    path('denuncia/<int:pk>/edit/', views.denuncia_edit, name='denuncia_edit'),
]