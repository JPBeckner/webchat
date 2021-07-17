from django.urls import path

from .views import index, room


app_name = 'chat'

urlpatterns = [
    path(route='', view=index, name='index'),
    path(route='<str:room_name>/', view=room, name='room')
]
