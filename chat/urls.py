from django.urls import path
from .views import*

urlpatterns = [
    path('<int:friend_id>/',chat,name='chat')
]
