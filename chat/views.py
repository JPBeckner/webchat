from django.shortcuts import render, redirect


def index(request):
    return render(request=request, template_name='chat/index.html')


def chat(request):
    return render(request=request, template_name='chat/chats.html')


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })
