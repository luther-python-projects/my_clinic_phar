from django.shortcuts import render


def register(request):
    data = {'title': 'registration'}
    return render(request, 'Accounts/register.html', context=data)


def sign_in(request):
    data = {'title': 'connect '}
    return render(request, 'Accounts/sign_in.html', context=data)


def sign_out(request):
    data = {'title': 'disconnect'}
    return render(request, 'Accounts/sign_out.html', context=data)


def pwd_forget(request):
    data = {'title': 'password forget'}
    return render(request, 'Accounts/pwd_forget.html', context=data)


def registration(request):
    data = {'title': 'registration'}
    return render(request, 'Accounts/registration.html', context=data)
