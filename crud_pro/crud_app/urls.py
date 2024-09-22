from django.urls import path
from .views import CrudApi

urlpatterns = [
    path('crudapi/', CrudApi.as_view(), name='crudapi'),
    path('crudapi/<int:pk>/', CrudApi.as_view(), name='crudapi'),
]