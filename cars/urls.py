from django.urls import path
from . import views

urlpatterns = [
    path("cars/", views.something),
    path("cars/<int:id>", views.something),
]

