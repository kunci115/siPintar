from django.shortcuts import render
from .model import respon
from .models import TextMessage
from .models import SipintarResponse, SipintarResponseModel


def index(request):
    return render(request, 'index.html', {
        'bot_message': "Halo ! chat untuk memulai",
        'display': "none"
    })


def submit(request):
    user_message = request.POST['user_message']
    TextMessage.objects.create(message=user_message)
    bot_message = executebotscript(user_message)
    SipintarResponse.objects.create(answer=bot_message[0],
                                    response_model=SipintarResponseModel.objects.create(tag=bot_message[1],
                                    context_set=bot_message[2]))
    return render(request, 'index.html', {
        'bot_message': bot_message[0],
        'user_message': user_message,
        'display': "block"
    })


def executebotscript(message):
    return respon.response(message)
