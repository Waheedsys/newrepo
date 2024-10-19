from django.urls import path
from . import views

urlpatterns = [
    path('', views.htop_view, name='htop'),
]
