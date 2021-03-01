from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.http import HttpResponse
from hod.forms import *
from django.contrib import messages
from django.contrib.auth import authenticate


def index(request):
    return render(request, "index.html")


def hod_register(request):
    # return render(request, "register.html")
    if request.method == 'POST':
        hod_username = request.POST["hod_username"]
        hod_password = request.POST["hod_password"]
        hod_email = request.POST['hod_email']
        form1 = HodForm(request.POST, request.FILES)
        form2 = clg_detail(request.POST)
        try:
            print(form1.is_valid(), form2.is_valid())
            for i in form2.data:
                print(i, type(i))
            if form1.is_valid() and form2.is_valid():
                form1.save()
                form2.save()
                user = User.objects.create_user(username=hod_email, password=hod_password, email=hod_email, first_name=hod_username)
                user.save()
                messages.info(request, "Data Saved Sucessfully")
                return redirect("/")
            else:
                return HttpResponse("Data not Saved \n")
        except Exception as e:
            return HttpResponse(f"Data not Saved with \n{e}")
    else:
        return render(request, "register.html")


def hod_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        print(user)
        user_data = hod_registration.objects.filter(hod_email=email, hod_password=password)
        print(user_data)
        valid = False
        username = ''
        for i in user_data:
            valid = i.hod_verification
            username = i.hod_username
            print(valid, username)
        print(valid, user)
        if user is not None and valid:
            auth.login(request, user)
            return render(request, "hod_dashboard.html", {'username' : username})
        else:
            messages.info(request, "Wrong email or password!!")
            return redirect("/")
    else:
        return render(request, "login.html")


def hod_dashboard(request):
    return render(request, "hod_dashboard.html")


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