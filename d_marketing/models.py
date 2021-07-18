from django.db import models

class Subscribing(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Subscribe'

    def __str__(self):
        return self.email
