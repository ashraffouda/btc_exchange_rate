from django.urls import path
from . import views

urlpatterns = [
    path("api/v1/quotes", views.get_exchange_entry),
]