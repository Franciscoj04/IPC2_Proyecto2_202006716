from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='front-home'),
    path('home/', views.home,name='front-home'),
    path('add/',views.add,name='add'),
    path('cargar/',views.cargaMasiva,name='carga'),
    path('ayuda/',views.ayuda,name='ayuda'),
    path('eliminar/',views.eliminar,name='eliminar'),
]