from django.db import models


# Create your models here.
class loginModel(models.Model):
    mobile = models.CharField(max_length=12)
    dateTime = models.DateTimeField()
    otp = models.CharField(max_length=10)


def __str__(self):
    return 'Mobile = {}, Time = {}, OTP = {}'.format(self.mobile, self.dateTime, self.otp)

class BookingSlotTable(models.Model):
    bst = models.TimeField('%H:%M')
    bet = models.TimeField('%H:%M')
    ppd = models.TimeField('%H:%M')