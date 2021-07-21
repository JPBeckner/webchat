from django.urls import path

from .views import register


app_name = 'bot'

urlpatterns = [
    path(route='register/', view=register, name='register'),
]
