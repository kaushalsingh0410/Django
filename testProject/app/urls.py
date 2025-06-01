from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', index,name='index'),
    path('<int:pk>/', index,name='index-update'),
    path('<int:pk>/', index,name='index-update'),
    path('delete/', delete,name='delete'),
    path('table/', table,name='table'),
]