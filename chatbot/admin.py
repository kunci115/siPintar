from django.contrib import admin
from .models import Text_Message
from .models import Sipintar_Response
from .models import Sipintar_Response_Model

admin.site.register(Text_Message)
admin.site.register(Sipintar_Response)
admin.site.register(Sipintar_Response_Model)