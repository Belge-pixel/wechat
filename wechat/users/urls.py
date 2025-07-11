from django.urls import path
from .views import*

urlpatterns = [
    path("",connexion , name="connexion"),
    path("inscription/",inscription,name="inscription")
]
