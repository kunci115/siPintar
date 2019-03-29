from django.db import models


class SipintarResponseModel(models.Model):
    tag = models.CharField(max_length=100)
    context_set = models.CharField(max_length=100)


class TextMessage(models.Model):
    message = models.CharField(max_length=250)

    def __str__(self):
        return self.message[0:5]


class SipintarResponse(models.Model):
    answer = models.CharField(max_length=250)
    response_model = models.ForeignKey(SipintarResponseModel, on_delete = models.CASCADE)
