from django.shortcuts import render
from django.http import HttpResponse
from hod.forms import *
from .models import *


def index(request):
    return render(request, "register.html")


def hod_register(request):
    if request.method == 'POST':
        form = HodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("\n\n\n\nData saved")
        return HttpResponse("Data Saved Sucessfully")