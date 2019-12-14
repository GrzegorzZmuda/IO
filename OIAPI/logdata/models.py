from django.db import models

# Create your models here.
class Logdata(models.Model):
    name = models.CharField(max_length=100)  #Nazwa Aplikacji z której pochodzą logi
    uptime = models.TimeField
    rpm = models.IntegerField
    meanlatency=models.TimeField
    cent99latency = models.TimeField
    cent999latency = models.TimeField
    err4xx = models.IntegerField
    err5xx = models.IntegerField
    created = models.DateTimeField(auto_now_add=True)
