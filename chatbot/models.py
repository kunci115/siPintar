from django.db import models


class Sipintar_Response_Model(models.Model):
    tag = models.CharField(max_length=100)
    context_set = models.CharField(max_length=100)


class Text_Message(models.Model):
    message = models.CharField(max_length=250)

    def __str__(self):
        return self.message[0:5]


class Sipintar_Response(models.Model):
    answer = models.CharField(max_length=250)
    response_model = models.ForeignKey(Sipintar_Response_Model, on_delete = models.CASCADE)
