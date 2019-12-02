from django.urls import path
from .views import *

urlpatterns = [
    path('create/location/<int:pk>',LocationUpdateView.as_view(), name='add_location'),


]


