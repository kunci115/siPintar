from django.db import models

class Bot_Response_Model(models.Model):
    tag = models.CharField(max_length = 100)
    context_set = models.CharField(max_length = 100)

class User_Message(models.Model):
    message = models.CharField(max_length = 250)

    def __str__(self):
        return self.message[0:5]


class Bot_Response(models.Model):
    answer = models.CharField(max_length = 250)
    response_model = models.ForeignKey(Bot_Response_Model, on_delete = models.CASCADE)