import os
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.http import HttpResponse
from faculty.models import temp_csv, faculty
from hod.forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, update_session_auth_hash
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
import pandas as pd
from django.core.mail import send_mail
from django.conf import settings




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
                        user = User.objects.create_user(username=hod_email, password=hod_password, email=hod_email, first_name=hod_username, last_name='1')
                        user.save()
                        subject = f"Thank you for registration {hod_username}"
                        message = "We are very happy that you join use.\nplease give use 24hr to complete your authentication and create your login credential.\nYou will also receve an email once you are verified\n\nThanks and Regards\nProject Evaluation System"
                        from_email = settings.EMAIL_HOST
                        to_list = [hod_email]
                        send_mail(subject, message, from_email, to_list, fail_silently=True)

                        user_data = hod_registration.objects.get(hod_email = hod_email)
                        id = user_data.id
                        gmail = user_data.hod_email
                        subject = f"Please Verify your E-mail Account "
                        message = f"Please verify your email by going to the following link\nhttp://127.0.0.1:8000/hod/email_verify/?id={id}&gmail={gmail}\n\nThanks and Regards,\nProject Evaluation System"
                        from_email = settings.EMAIL_HOST
                        to_list = [hod_email]
                        send_mail(subject, message, from_email, to_list, fail_silently=True)
                        print("\n\n\nGMAIL HAS BEEN SEND")
                        return render(request, "password/email_verify_send.html")

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
            user = authenticate(username=email, password=str(password))
            print(user)
            user_data = hod_registration.objects.filter(hod_email=email)
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
    loc = ''
    faculty_in_system = []
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
                            check = 0
                            if User.objects.filter(email=f):
                                check=1
                                user1 = faculty.objects.create(fullname=a, username=b, password=c,college_name=request.user.last_name,college_department_name=e, subjects=d, user_type=2,faculty_email=f, hod_email=request.user.email)
                                # faculty_in_system.append(f)
                            if check==0:
                                user1 = faculty.objects.create(fullname=a, username=b, password=c,college_name=request.user.last_name, college_department_name=e,subjects=d, user_type=2, faculty_email=f, hod_email=request.user.email)
                                user2 = User.objects.create_user(username=f, password=c, first_name=a, email=f, last_name='2')
                            user = hod_registration.objects.filter(hod_email=request.user.email)
                            hod_name = ''
                            hod_clg = ''
                            for i in user:
                                hod_name = i.hod_fullname
                                print(hod_name)
                                hod_clg = i.college_name
                                print(hod_clg)
                            # send mails("subject","message", "from_mail", "to_list", "fail_silentry=True")
                            subject = f"Congratulations you are Registered to our system by {hod_name} from {hod_clg}"
                            message = f"You are Registered for Subject {d} as faculty and now you may access all our functionality\nYour Login credentials:\nRegistered Email = {f}\nYour password = {c}\n\nThanks and regards\nHOD {hod_name}"
                            from_email = settings.EMAIL_HOST
                            to_list = [f'{f}']
                            send_mail(subject, message, from_email, to_list , fail_silently=True)
                            user1.save()
                            if check==0:
                                user2.save()
                        messages.info(request, "All the Faculty are saved Sucessfully")
                        temp_csv.objects.filter(hod_name=request.user.email).delete()
                        return render(request, "add_faculty.html")
                    except Exception as e:
                        return HttpResponse(f"Error while adding faculty error {e}")
                    return HttpResponse("Save")
            return HttpResponse("Please give Department Name")
        else:
            return render(request, "add_faculty.html")
    else:
        return HttpResponse("Please Login First")


def register_faculty(request):
    return redirect('/')


def faculty_desc(request):
    faculty_info = faculty.objects.filter(hod_email = request.user.email)
    return render(request, 'faculty_desc.html', {'faculty_info':faculty_info})


def edit_faculty(request):
    if request.method == 'POST':
        id = request.POST['id']
        data = faculty.objects.get(id=id)
        data.fullname = request.POST['fac_fname']
        data.username = request.POST['fac_uname']
        data.faculty_email = request.POST['fac_email']
        data.college_department_name = request.POST['fac_dep']
        data.subjects = request.POST['fac_sub']
        data.save()
        messages.info(request, "Data saved SucessFully")
        faculty_info = faculty.objects.all()
        return render(request, 'faculty_desc.html', {'faculty_info':faculty_info})
    else:
        id = request.GET["id"]
        faculty_into = faculty.objects.filter(id=id)
        for i in faculty_into:
            print(i.username)
        return render(request, "faculty_info.html", {"faculty_into":faculty_into})


def profile(request):
    if request.method == "POST":
        user_info = hod_registration.objects.filter(hod_email=request.POST['fac_email'])
        id = request.POST['id']
        data = hod_registration.objects.get(id=id)
        data.hod_fullname = request.POST['fac_fname']
        data.hod_username = request.POST['fac_uname']
        data.hod_email = request.POST['fac_email']
        data.hod_phone_number = request.POST['fac_pno']
        data.hod_password = request.POST["fac_pass"]
        data1 = User.objects.get(username = request.user.username)
        data1.first_name = request.POST['fac_uname']
        data1.email = request.POST["fac_email"]
        data1.username = request.POST["fac_email"]
        temp_pass = str(request.POST["fac_pass"])
        print(temp_pass, type(len(temp_pass)))
        print(len(temp_pass)==2, len(temp_pass)==1, len(temp_pass)==0)
        check = 0
        if len(temp_pass)!=0 and len(temp_pass)>=3:
            print(temp_pass, type(temp_pass))
            data1.set_password(temp_pass)
            update_session_auth_hash(request, data1)
            print("password saved")
            check = 1
            # return render(request, 'profile.html', {'user_info': user_info})
        if len(temp_pass)==2 or len(temp_pass)==1 or len(temp_pass)==0:
            print("here in too small")
            messages.info(request, 'Password is too small try again with different password')
        data.save()
        data1.save()
        if check ==1:
            messages.info(request, "Data saved SucessFully")
        else:
            messages.info(request, "All the fields are saved without Password")
        return render(request, 'profile.html', {'user_info': user_info})
    else:
        email = request.user.email
        print(email)
        user_info = hod_registration.objects.filter(hod_email=email)
        # for i in user_info:
        #     print(i.username)
        return render(request, "profile.html", {"user_info": user_info})


def password_reset(request):
    return render(request, "password_reset_email.html")


def email_verify(request):
    if request.method == 'POST':
        print("\n\n\nIN POST METHOD")
        a = request.POST['id']
        b = request.POST["gmail"]
        subject = f"Congratulations you are Registered"
        message = f"Please verify your email by going to the following link\nhttp://127.0.0.1:8000/hod/email_verify/?id={a}&gmail={b}\n\nThanks and Regards,\nProject Evaluation System"
        from_email = settings.EMAIL_HOST
        to_list = [f'{b}']
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        print("\n\n\nGMAIL HAS BEEN SEND")
        return render(request, "password/email_verify_send.html")
    else:
        aa = request.GET['id']
        bb = request.GET['gmail']
        print(aa, bb)
        hod_data = hod_registration.objects.get(id=aa, hod_email=bb)
        print(hod_data)
        # print(user.hod_verification)

        print(f"\n\n\nHOD VERIFICATION =  {hod_data.hod_verification}")
        hod_data.hod_verification = True
        print(f"\n\n\nHOD VERIFICATION =  {hod_data.hod_verification}")

        hod_data.save()
        # verified = "verified"
        messages.info(request, "Congratulations your email is verified Successful")
        return render(request, "index.html")






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


