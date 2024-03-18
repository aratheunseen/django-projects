from django.urls import path
from . import views

urlpatterns = [
    path('application/', views.index, name='index'),
]