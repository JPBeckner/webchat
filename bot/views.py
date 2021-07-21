from re import findall

from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib import messages
from .models import Bot
from asgiref.sync import sync_to_async
from requests import post


def register(request: HttpRequest):
    if request.method == "POST":
        name = request.POST.get('name', '')
        url = request.POST.get('url', '')
        command = request.POST.get('command', '')

        if any(empty_value(value) for value in [name, url, command]):
            messages.error(request=request, message="Empty value(s)")
            return redirect('bot:register')

        if Bot.objects.filter(name=name).exists():
            messages.error(request=request, message="Bot already exists")
            return redirect(to='bot:register')

        
        Bot.objects.create(
            name=name,
            url=url,
            command=command
        ).save()
        
        return redirect('chat:index')

    return render(
        request=request, 
        template_name='bot/register.html',
    )



def check_bot_command(function):
    async def wrapper(chat, event):

        await function(chat, event)

        # check if there is a bot command on the message.
        commands = get_command_from_message(message=event['message'])
        if not commands:
            return

        command, parameter = commands.pop(0)

        # check if the command provided refer to some avaliable bot.
        bot = await sync_to_async(Bot.objects.filter)(command=command)
        if not await sync_to_async(len)(bot):
            return

        # send the command to the bot called.
        await sync_to_async(
            func=send_command
        )(url=bot[0].url, command=command, parameter=parameter, room=event.get('room', ''))

    return wrapper


def send_command(url: str, command: str, parameter: str, room: str):
    post(
        url=url,
        json={
            'command': command,
            'parameter': parameter,
            'room': room
        }
    )


def empty_value(value: str) -> bool:
    return not bool(value.strip())


def get_command_from_message(message: str) -> list:
    return findall(r"\/(.*)=(.*)", message)
