from django.urls import path
from . import views

urlpatterns = [
    path('', views.symptom_check, name='symptom_check'),
]
