from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User


def index(request):
    return render(request=request, template_name='chat/index.html')


def join(request):
    if request.user.is_authenticated:
        return render(request=request, template_name='chat/join.html')
    return redirect('user:login')


def room(request, room_name):
    if request.user.is_authenticated:
        return render(
            request=request,
            template_name='chat/room.html', 
            context={
                'room_name': room_name,
            }
        )
    return redirect('user:login')
