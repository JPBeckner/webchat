from django.urls import path

from .views import chat, index, room


app_name = 'chat'

urlpatterns = [
    path(route='', view=index, name='index'),
    path(route='chat/', view=chat, name='chat'),
    path(route='<str:room_name>/', view=room, name='room')
]
