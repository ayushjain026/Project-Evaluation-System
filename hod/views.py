from django.shortcuts import render
from django.http import HttpResponse
from hod.forms import *
from .models import *


def index(request):
    return render(request, "index.html")


def hod_register(request):
    if request.method == 'POST':
        form = HodForm(request.POST, request.FILES)
        try:
            print(form.is_valid())
            if True:
                form.save()
                print("\n\n\n\nData saved")
                return HttpResponse("Data Saved Sucessfully")
            else:
                return HttpResponse("Data not Saved Sucessfully")
        except Exception as e:
            return HttpResponse(f"Data not Saved Sucessfully\n{e}")