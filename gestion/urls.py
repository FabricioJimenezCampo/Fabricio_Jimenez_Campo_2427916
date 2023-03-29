from django.urls import path
from . import views

urlpatterns = [
    path('', views.Pagina),
    path('otro/', views.opcion),
]
    