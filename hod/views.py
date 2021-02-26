from django.shortcuts import render, redirect
from django.http import HttpResponse
from hod.forms import *
from .models import *


def index(request):
    return render(request, "index.html")


def hod_register(request):
    # return render(request, "register.html")
    if request.method == 'POST':
        form1 = HodForm(request.POST, request.FILES)
        form2 = clg_detail(request.POST)
        try:
            print(form1.is_valid(), form2.is_valid())
            for i in form2.data:
                print(i, type(i))
            if form2.is_valid():
                form1.save()
                form2.save()
                print("\n\n\n\nBoth the Data saved")
                return HttpResponse("Data Saved Sucessfully")
            else:
                return HttpResponse("Data not Saved ")
        except Exception as e:
            return HttpResponse(f"Data not Saved with \n{e}")
    else:
        return render(request, "register.html")


def test(request):
    return render(request, "test.html")


def test_save(request):
    if request.method == 'POST':
        form = testForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            print("\n\ndata saved\n\n")
    else:
        form = testForm()
    return render(request, 'test.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')