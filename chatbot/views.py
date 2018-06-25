from django.shortcuts import render
from .model import respon


def index(request):
	return render(request, 'index.html', {
        'botMessage': "Halo ! chat untuk memulai",
        'display': "none"
      })

def submit(request):
    userMessage = request.POST['userMessage']
    botMessage = executebotscript(userMessage)
    return render(request, 'index.html', {
        'botMessage': botMessage,
        'userMessage': userMessage,
        'display': "block"
      })

def executebotscript(message):
    return respon.response(message)
