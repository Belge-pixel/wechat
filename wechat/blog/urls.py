from django.urls import path
from .views import*

urlpatterns = [
    path('',blog,name='blog'),
    path('detail/<str:slug>',detail,name='detail')
]
