from django.contrib import admin
from .models import User_Message
from .models import Bot_Response
from .models import Bot_Response_Model

admin.site.register(User_Message)
admin.site.register(Bot_Response)
admin.site.register(Bot_Response_Model)