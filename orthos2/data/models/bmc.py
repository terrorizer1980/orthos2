from django.db import models
from . import NetworkInterface
class BMC(models.Model):
    username = models.CharField(max_length=256, name="BMC User", blank=True)
    password = models.CharField(max_length=256, name="BMC Password", blank=True)
    network_interface = models.OneToOneField(NetworkInterface, on_delete=models.CASCADE, primary_key=True)
    machine = models.ForeignKey('data.Machine', on_delete=models.CASCADE)