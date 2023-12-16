import datetime

from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def isitchristmas(request):
    today = datetime.datetime.now()
    context = {
        "christmas": today.month == 12 and today.day == 25
    }
    return render(request, 'checkChristmas/index.html', context)