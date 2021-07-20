from django.shortcuts import redirect, render
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import HttpRequest


def login(request: HttpRequest):
    if request.method == "POST":
        username = request.POST.get('name')
        password = request.POST.get('password')

        if any(empty_value(value) for value in [username, password]):
            messages.error(request=request, message="Empty value(s)")
            return redirect(to='user:login')

        if User.objects.filter(username=username).exists():
            user = auth.authenticate(
                request=request,
                username=username,
                password=password
            )
            if user is not None:
                auth.login(request=request, user=user)
                print('login success')
                request.session['username'] = username
                return redirect(to='chat:join')



    return render(request=request, template_name='user/login.html')


def logout(request):
    auth.logout(request=request)
    return redirect(to='chat:index')


def register(request: HttpRequest):
    if request.method == "POST":
        username = request.POST.get('name')
        password = request.POST.get('password')

        if any(empty_value(value) for value in [username, password]):
            messages.error(request=request, message="Empty value(s)")
            return redirect('user:register')

        if User.objects.filter(username=username).exists():
            messages.error(request=request, message="User already exists")
            return redirect(to='user:register')

        
        user = User.objects.create_user(
            username=username,
            password=password
        )
        user.save()
        messages.success(request=request, message="User registered successfully")
        
        return redirect('user:login')

    return render(
        request=request, 
        template_name='user/register.html',
    )


def empty_value(value: str) -> bool:
    return not bool(value.strip())
