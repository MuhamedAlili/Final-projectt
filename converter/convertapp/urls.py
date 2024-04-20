from django.contrib import admin
from django.urls import path, include
from .views import convert_currency

urlpatterns = [
    path('', convert_currency, name='convert_currency'),
]