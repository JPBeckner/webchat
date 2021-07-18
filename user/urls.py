from django.urls import path

from .views import login, register


app_name = 'user'

urlpatterns = [
    path(route='login/', view=login, name='login'),
    path(route='register/', view=register, name='register'),
]
