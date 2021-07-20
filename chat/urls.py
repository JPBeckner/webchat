from django.urls import path

from .views import join, index, room


app_name = 'chat'

urlpatterns = [
    path(route='', view=index, name='index'),
    path(route='chat/join/', view=join, name='join'),
    path(route='chat/<str:room_name>/', view=room, name='room')
]
