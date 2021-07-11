from django.contrib import admin
from django.urls import path

from start.views import f_start

urlpatterns = [
    path('', f_start)
]