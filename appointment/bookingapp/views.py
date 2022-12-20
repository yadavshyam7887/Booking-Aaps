from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta
from pytz import timezone

# from . import models
from .models import loginModel, BookingSlotTable
from . import utilities as ut
import pytz

# time
# Create your views here.
def index(request):
    if request.GET:
        mobile = request.GET['mobile']
        getOtp = ut.generateOtp(5)
        # ut.mailSend()

        #Delete all previous mobile data
        # previous = \
        loginModel.objects.filter(mobile = mobile).delete()
        # if previous != 0:
        #     previous.delete()

        date = datetime.now() + timedelta(minutes=5)
        data = loginModel()
        data.mobile = mobile
        data.otp = getOtp
        data.dateTime = date
        data.save()
        return render(request, "otpVerification.html", {"mobile": mobile})

    return render(request, "index.html")


def otp(request):
    getOtp = ut.generateOtp(5)
    return HttpResponse(getOtp)


def otpVerification(request):
    print ('Here')
    userotp = request.GET['otpverification']

    if request.GET:
        mobile = request.GET['mobile']
        userotp = request.GET['otpverification']
        data = loginModel.objects.filter(mobile=mobile)
        print (data[0].dateTime)
        print (data[0].otp)
        currdate = datetime.now()
        maxDate = data[0].dateTime
        utc = pytz.UTC

        c = utc.localize(currdate)

        if userotp == data[0].otp and c < maxDate:
            return HttpResponse("Account Successfully Created")


        return HttpResponse("Mismatch OTP")

    return render(request, "otpVerification.html")

def bookingPage(request):
    if request.GET:
        bst = request.GET['bst']
        bet = request.GET['bet']
        ppd = request.GET['ppd']
        data = BookingSlotTable()
        bst = data.bst
        bst = data.bet
        ppd = data.ppd
        data.save()
    return render(request, "bookingPage.html")