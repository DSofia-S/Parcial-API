from django.urls import path
from .views import AutorList

urlpatterns = [
    path('autores/', AutorList.as_view(), name='persona-list'),
]