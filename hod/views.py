import csv
import io
import os

from django.conf import settings
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.http import HttpResponse

from faculty.models import temp_csv, faculty
from hod.forms import *
from django.contrib import messages
from django.contrib.auth import authenticate
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
import pandas as pd


def index(request):
    return render(request, "index.html")


def hod_register(request):
    if request.method == 'POST':
        hod_username = request.POST["hod_username"]
        hod_password = request.POST["hod_password"]
        hod_email = request.POST['hod_email']
        user_type = request.POST['user_type']
        number1 = request.POST['hod_phone_number']
        number2 = request.POST['college_phone_number']
        form1 = HodForm(request.POST, request.FILES)
        form2 = clg_detail(request.POST)
        if len(number1)<=12 and len(number1)>=8 and len(number2)<=12 and len(number2)>=8:
            try :
                temp1 = int(number1)
                temp2 = int(number2)
                try:
                    print(form1.is_valid(), form2.is_valid())
                    for i in form2.data:
                        print(i, type(i))
                    if form1.is_valid() and form2.is_valid():
                        form1.save()
                        form2.save()
                        user = User.objects.create_user(username=hod_email, password=hod_password, email=hod_email, first_name=hod_username, user_type=user_type)
                        user.save()
                        messages.info(request, "Data Saved Sucessfully")
                        return redirect("/")
                    else:
                        return HttpResponse("Data not Saved \n")
                except Exception as e:
                    return HttpResponse(f"Data not Saved with \n{e}")
            except Exception as e:
                messages.info(request, "Please Enter valid Number")
                return render(request, "register.html")
        else:
            messages.info(request, "Please Enter valid Number")
            return render(request, "register.html")
    else:
        return render(request, "register.html")


@ensure_csrf_cookie
@csrf_protect
def hod_login(request):
    if request.user.is_authenticated == False:
        if request.method == "POST":
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(username=email, password=password)
            print(user)
            user_data = hod_registration.objects.filter(hod_email=email, hod_password=password)
            # print(user_data)
            valid = False
            for i in user_data:
                valid = i.hod_verification
                print(valid)
            print(valid, user)
            if user is not None and valid:
                auth.login(request, user)
                return render(request,"hod_dashboard.html")
            else:
                messages.info(request, "Wrong email or password!!")
                return redirect("/")
        else:
            return render(request, "login.html")
    else:
        return render(request, "hod_dashboard.html")


def hod_dashboard(request):
    return render(request, "hod_dashboard.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def add_faculty(request):
    if request.user.is_authenticated:
        if request.method == "POST": #and request.FILES['faculty_register']:
            department = request.POST["department"]
            if request.method == 'POST':
                form = csvForm(request.POST, request.FILES)
                print("Getting form")
                print(form.is_valid())
                if form.is_valid():
                    print("it is valid")
                    form.save()
                    a = request.user
                    print(a.username)
                    file_data = temp_csv.objects.filter(hod_name=request.user.username)
                    print(file_data)
                    for i in file_data:
                        loc = i.csv_file
                        print(i.csv_file, i.hod_name, type(i.hod_name))
                    base_dir = settings.MEDIA_ROOT
                    my_file = os.path.join(base_dir, str(loc))
                    print(my_file)
                    df = pd.read_csv(f'{my_file}')
                    print(df)
                    try:
                        length = len(df)
                        print(length)
                        for i in range(length):
                            a = df["Faculty Name"][i]
                            b = df["Faculty username or enrolnment no"][i]
                            c = df["Password"][i]
                            c = str(c)
                            d = df["Subject"][i]
                            e = df["Department"][i]
                            f = df["Email Id"][i]
                            user1 = faculty.objects.create(fullname=a, username=b, password=c,college_name=request.user.last_name, college_department_name=e,subjects=d, user_type=2, faculty_email=f)
                            user2 = User.objects.create_user(username=b, password=c, first_name=a, last_name=request.user.last_name, email=f)
                            user1.save()
                            user2.save()
                        messages.info(request, "All the Faculty are saved Sucessfully")
                        temp_csv.objects.filter(hod_name=request.user.email).delete()
                        return render(request, "add_faculty.html")
                    except Exception as e:
                        return HttpResponse(f"Error while adding faculty error {e}")
                    return HttpResponse("Save")


            return HttpResponse("Error")
            # for i in range(3, sheet.nrows):
            #     try:
            #         get_test_data=sheet.row_values(i)[1]
            #         print(get_test_data)
            #         return HttpResponse(request, "Data saved")
            #     except:
            #         print("an error occured")
            #         return HttpResponse(request, "Error")
        else:
            return render(request, "add_faculty.html")
    else:
        return HttpResponse("Please Login First")


def register_faculty(request):

    return redirect('/')


def test(request):
    return render(request, "base_hod.html")


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


