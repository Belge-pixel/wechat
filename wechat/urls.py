from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',include('home.urls')),
    path('chat/',include('chat.urls')),
    path('forum/',include('forum.urls')),
    path('blog/',include('blog.urls')),
    path('',include('users.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)