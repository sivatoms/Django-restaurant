from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
# Create your models here.

class Reservation(models.Model):
    LastName = models.CharField(max_length=100)
    FirstName = models.CharField(max_length=100)
    NumberOfGuests = models.IntegerField(default=0)
    ReserveDate = models.DateTimeField(default=timezone.now)
    Time = models.TimeField(default=datetime.now())

