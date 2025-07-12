from django.urls import path
from .views import*

urlpatterns = [
    path('',home,name='home'),
    path('ajouter/<int:slug>/',ajouter,name='ajouter'),
    path('amis/<int:slug>/',amis,name='amis'),
    path('profile/<int:slug>/',profile,name="profile")
]
