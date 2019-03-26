from django.shortcuts import render
from .model import respon


def index(request):
    return render(request, 'index.html', {
        'bot_message': "Halo ! chat untuk memulai",
        'display': "none"
      })


def submit(request):
    user_message = request.POST['user_message']
    bot_message = executebotscript(user_message)
    return render(request, 'index.html', {
        'bot_message': bot_message,
        'user_message': user_message,
        'display': "block"
      })


def executebotscript(message):
    return respon.response(message)
