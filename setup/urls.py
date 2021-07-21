from django.conf import urls
from django.conf.urls import include
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('', include('chat.urls', namespace='chat')),
    path('user/', include('user.urls', namespace='user')),
    path('bot/', include('bot.urls', namespace='bot')),
    path('admin/', admin.site.urls),
]
