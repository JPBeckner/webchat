from django.urls import path

from .views import login, register, logout


app_name = 'user'

urlpatterns = [
    path(route='login/', view=login, name='login'),
    path(route='logout/', view=logout, name='logout'),
    path(route='register/', view=register, name='register'),
]
