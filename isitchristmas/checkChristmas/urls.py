
from django.urls import path

from . import views

urlpatterns = [
    path('', views.isitchristmas, name="check"),
]