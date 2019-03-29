from django.contrib import admin
from .models import TextMessage
from .models import SipintarResponse
from .models import SipintarResponseModel

admin.site.register(TextMessage)
admin.site.register(SipintarResponse)
admin.site.register(SipintarResponseModel)