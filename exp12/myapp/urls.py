# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('check/', views.check_odd_even, name='check_odd_even'),
    path('filter/', views.name_filter, name='name_filter'),
]
