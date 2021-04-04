import os
import pandas as pd
from django.contrib import auth
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
# Create your views here.
# data = user.objects.get()
from faculty.forms import csvForm_faculty, create_submission_form
from faculty.models import temp_csv, faculty, evaltation_generate, notice
from hod.models import hod_registration
from project_management_system import settings
from student.models import temp_csv_for_students, student, student_subjects, work_histort, event_submission


def dashboard(request):
    return render(request, "dashboard.html")


def add_student(request):
    loc = ''
    print("in add student ")
    clg_name = ''
    faculty_in_system = []
    if request.user.is_authenticated and request.user.last_name=='2':
        if request.method == "POST":  # and request.FILES['faculty_register']:
            sem = request.POST["sem"]
            print(sem)
            if request.method == 'POST':
                form = csvForm_faculty(request.POST, request.FILES)
                print("Getting form")
                print(form)
                print(form.is_valid())
                if form.is_valid():
                    print("it is valid")
                    form.save()
                    a = request.user
                    print(a.username)
                    file_data = temp_csv_for_students.objects.filter(faculty_name=request.user.username)
                    print(file_data)
                    for i in file_data:
                        loc = i.csv_file
                        print(i.csv_file, i.faculty_name, type(i.faculty_name))
                    base_dir = settings.MEDIA_ROOT
                    my_file = os.path.join(base_dir, str(loc))
                    print(my_file)
                    df = pd.read_csv(f'{my_file}')
                    print(df)
                    try:
                        print('')
                        length = len(df)
                        print(length)
                        for i in range(length):
                            a = df["Student Name"][i]
                            b = df["Enrollnment no"][i]
                            c = df["Password"][i]
                            c = str(c)
                            d = df["Subject"][i]
                            e = df["Department"][i]
                            f = df["Email Id"][i]
                            g = df["Group"][i]
                            h = df['Project Defination'][i]
                            check = 0
                            print("Faculty : ")
                            current_faculty = faculty.objects.filter(faculty_email=request.user.email)
                            print("")
                            print(current_faculty)
                            for i in current_faculty:
                                current_faculty = i
                                print("break")
                                break
                            print(current_faculty.college_name)
                            # for i in current_faculty:
                            clg_name = current_faculty.college_name
                            print(current_faculty.college_name)
                            if User.objects.filter(email=f):
                                check = 1
                                # user1 = student.objects.create(fullname=a, username=b, password=c, hod_email=current_faculty.hod_email,
                                #                                department=e, subjects=d, user_type=3,project_defination=h,
                                #                                student_email=f, faculty_email=request.user.email,
                                #                                verification=True, group=g, college_name=clg_name, semister=sem)
                                student_sub = student_subjects.objects.create(subject=d, faculty=request.user.email, student_id=f, hod=current_faculty.hod_email)
                            if check == 0:
                                user1 = student.objects.create(fullname=a, username=b, password=c,
                                                               college_name=clg_name, hod_email=current_faculty.hod_email,
                                                               department=e, subjects=d, user_type=3,project_defination=h,
                                                               student_email=f, faculty_email=request.user.email,
                                                               verification=False, group=g, semister=sem)
                                user2 = User.objects.create_user(username=f, password=c, first_name=a, email=f,
                                                                 last_name='3')
                                student_sub = student_subjects.objects.create(subject=d, faculty=request.user.email,
                                                                              student_id=f,
                                                                              hod=current_faculty.hod_email)

                            user = faculty.objects.filter(faculty_email=request.user.email)
                            faculty_name = ''
                            clg = ''
                            for i in user:
                                faculty_name = i.fullname
                                print(faculty_name)
                                clg = i.college_name
                                break
                            # send mails("subject","message", "from_mail", "to_list", "fail_silentry=True")
                            subject = f"Congratulations you are Registered to our system by {faculty_name} from {clg} for Subject {d}"
                            message = f"You are Registered for Subject {d} as student and now you may access all our functionality\nYour Login credentials:\nRegistered Email = {f}\nYour password = {c}\nAlso Please verify your Email id if you have not verified\n\nThanks and regards\nFaculty {request.user.first_name}"
                            from_email = settings.EMAIL_HOST
                            to_list = [f'{f}']
                            send_mail(subject, message, from_email, to_list, fail_silently=True)

                            student_sub.save()
                            if check == 0:
                                user1.save()
                                user2.save()
                                user_data = student.objects.get(student_email=f)
                                id = user_data.id
                                gmail = user_data.student_email
                                subject = f"Please Verify your E-mail Account "
                                message = f"Please verify your email by going to the following link\nhttp://127.0.0.1:8000/student/email_verify/?id={id}&gmail={gmail}\n\nThanks and Regards,\nProject Evaluation System"
                                from_email = settings.EMAIL_HOST
                                to_list = [f]
                                send_mail(subject, message, from_email, to_list, fail_silently=True)
                                print("\n\n\nGMAIL HAS BEEN SEND")
                        messages.info(request, "All the Students are saved Sucessfully")
                        temp_csv_for_students.objects.filter(faculty_name=request.user.username).delete()
                        return render(request, "faculty/add_student.html")
                    except Exception as e:
                        return HttpResponse(f"Error while adding faculty error {e}")
            messages.info("Something went wrong Please try again")
            return render(request, "error.html")
        else:
            return render(request, "faculty/add_student.html")
    else:
        messages.info("You does not have required login credentials please login again or with different Id")
        return render(request, "error.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def student_desc(request):
    student_info = student.objects.filter(faculty_email=request.user.email)
    return render(request, "faculty/student_desc.html", {'student_info': student_info})


def email_verify(request):
    aa = request.GET['id']
    bb = request.GET['gmail']
    print(aa, bb)
    faculty_data = student.objects.get(id=aa, faculty_email=bb)
    print(faculty_data)
    # print(user.hod_verification)

    print(f"\n\n\nHOD VERIFICATION =  {faculty_data.verification}")
    faculty_data.erification = True
    print(f"\n\n\nHOD VERIFICATION =  {faculty_data.verification}")

    faculty_data.save()
    # verified = "verified"
    messages.info(request, "Congratulations your email is verified Successful")
    return render(request, "index.html")


def delete_student(request):
    id = request.GET["id"]
    user = student.objects.get(id=id)
    user1 = User.objects.get(email=user.student_email)
    user.delete()
    user1.delete()
    student_info = student.objects.filter(student_email=request.user.email)
    return render(request, "faculty/student_desc.html", {'student_info': student_info})


def edit_student(request):
    if request.method == 'POST':
        id = request.POST['id']
        data = student.objects.get(id=id)
        data.fullname = request.POST['fac_fname']
        data.username = request.POST['fac_uname']
        data.student_email = request.POST['fac_email']
        data.department = request.POST['fac_dep']
        # data.subjects = request.POST['fac_sub']
        data.semister = request.POST['fac_sem']
        data.save()
        messages.info(request, "Data saved SucessFully")
        faculty_into = student.objects.filter(id=id)
        for i in faculty_into:
            print(i.username)
        return render(request, "faculty/student_info.html", {"faculty_into": faculty_into})
    else:
        id = request.GET["id"]
        student_email_id=''
        faculty_into = student.objects.filter(id=id)
        for i in faculty_into:
            print(i.username)
            student_email_id = i.student_email
        sub = student_subjects.objects.filter(student_id=student_email_id)
        return render(request, "faculty/student_info.html", {"faculty_into":faculty_into, "sub":sub})


def edit_event(request):
    if request.method == 'POST':
        id = request.POST['id']
        data = evaltation_generate.objects.get(id=id)
        data.submission_title = request.POST['event_title']
        data.for_semister = request.POST['event_sem']
        data.submission_file_description = request.POST['event_description']
        # try:
        #     data.created_date = request.POST['event_stat_date']
        # except:
        #     print("")
        # try:
        #     data.submission_last_date = request.POST['event_last_date']
        # except:
        #     print("")
        print(f"\n\n\n\n\n{request.POST['event_stat_date']}\n\n")
        if request.POST['event_stat_date']:
            data.created_date = request.POST['event_stat_date']
        else:
            data.created_date = data.created_date
            print(data.created_date)
        if request.POST['event_last_date']:
            data.submission_last_date = request.POST['event_last_date']
        else:
            data.created_date = data.created_date
            print(data.created_date)
        data.submission_comment_faculty = request.POST['event_comment']
        data.submission_marks = request.POST['event_marks']
        data.save()
        messages.info(request, "Data saved SucessFully")
        faculty_into = student.objects.filter(id=id)
        for i in faculty_into:
            print(i.username)
        data = evaltation_generate.objects.filter(faculty_email_auth=request.user.email)
        return render(request, "faculty/total_events.html", {"data": data})
    else:
        event_info = evaltation_generate.objects.filter(id=request.GET["id"])
        print(event_info)
        return render(request, "faculty/event_info.html", {"event_info": event_info})



def profile(request):
    if request.method == "POST":
        user_info = faculty.objects.filter(hod_email=request.POST['fac_email'])
        id = request.POST['id']
        data = faculty.objects.get(id=id)
        data.fullname = request.POST['fac_fname']
        data.username = request.POST['fac_uname']
        data.email = request.POST['fac_email']
        # data.subjects = request.POST['fac_pno']
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
        if len(temp_pass)==2 or len(temp_pass)==1:
            print("here in too small")
            messages.info(request, 'Password is too small try again with different password')
        data.save()
        data1.save()
        dep = []
        for user in user_info:
            print(user.subjects)
            dep.append(user.subjects)
        if check ==1:
            messages.info(request, "Data saved SucessFully")
        else:
            messages.info(request, "All the fields are saved without Password")
        user_info = faculty.objects.filter(faculty_email=request.user.email)
        a = user_info[0].id
        user_info = faculty.objects.filter(id=a)
        dep = []
        for user in user_info:
            print(user.subjects)
            dep.append(user.subjects)
        print(dep)
        return render(request, "faculty/profile.html", {"user_info": user_info, "dep":dep})
    else:
        user_info = faculty.objects.filter(faculty_email=request.user.email)
        print(user_info)
        dep=[]
        for user in user_info:
            print(user.subjects)
            dep.append(user.subjects)
        print(dep)

        print(user_info[0].id, type(user_info))
        a = user_info[0].id
        user_info=faculty.objects.filter(id=a)
        print(user_info)
        # user_info = user_info[0]
        # return render(request, "faculty/profile.html", {"user_info": user_info})
        return render(request, "faculty/profile.html", {"user_info": user_info, "dep":dep})


def evaluation(request):
    data = evaltation_generate.objects.filter(faculty_email_auth=request.user.email)
    user_count = student.objects.filter(faculty_email=request.user.email)
    count = len(user_count)
    return render(request, "faculty/evaluation.html", {"total_events":len(data), "count":count})


def total_events(request):
    data = evaltation_generate.objects.filter(faculty_email_auth=request.user.email)
    return render(request, "faculty/total_events.html", {"data" : data})


def create_submission(request):
    if request.user.is_authenticated and request.user.last_name == '2':
        if request.method == "POST":
            fac = faculty.objects.filter(faculty_email=request.user.email)
            fac = fac[0]
            a = request.POST["submission_title"]
            b = request.POST["for_semister"]
            c = request.POST["submission_marks"]
            form = create_submission_form(request.POST)
            print("Getting form")
            print(form)
            print(form.is_valid())
            if form.is_valid():
                form.save()
                sub_comm_fac = request.POST['submission_comment_faculty']
                data = evaltation_generate.objects.get(submission_marks=c, for_semister=b, submission_title=a, faculty_email_auth=request.user.email)
                data.submission_comment_faculty = sub_comm_fac
                data.hod_email_auth = fac.hod_email
                data.submission_department = fac.department
                data.save()
                messages.info(request, "Event Generated Sucessfully")
                return render(request, "faculty/evaluation.html")
            else:
                messages.info(request, "Something Went Wrong")
                return render(request, "faculty/evaluation.html")
        else:
            messages.info(request, "Cant get POST")
            return render(request, "faculty/evaluation.html")
    else:
        messages.info(request, "Please check your user credentials")
        return render(request, "faculty/evaluation.html")


def delete_event(request):
    user = evaltation_generate.objects.get(id=request.GET["id"])
    user.delete()
    data = evaltation_generate.objects.filter(faculty_email_auth=request.user.email)
    return render(request, "faculty/evaluation.html", {"total_events": len(data)})


def create_notice(request):
    global notice_create
    if request.method == 'POST':
        print("In POST of note")
        form_title = request.POST['notice_title']
        form_desc = request.POST['notice_desc']
        user = faculty.objects.get(faculty_email=request.user.email)
        faculty_email = user.faculty_email
        hod_email = user.hod_email
        created_name = user.fullname
        for_sem = request.POST['sem']
        if for_sem == '0':
            for i in range(1,9):
                notice_create = notice.objects.create(note_title=form_title, note_description=form_desc , for_semister=i, faculty_email_auth=faculty_email, user_who_created_notice=created_name, hod_email_auth=hod_email, submission_department=user.department)
            notice_create.save()
            messages.info(request, "Notice Created Sucessfully")
            notices = notice.objects.filter(faculty_email_auth=request.user.email, user_who_created_notice=request.user.first_name)
            return render(request, "faculty/create_notice.html", {'notices':notices})
        else:
            notice_create = notice.objects.create(note_title=form_title, note_description=form_desc, for_semister=int(for_sem), faculty_email_auth=faculty_email, user_who_created_notice=created_name, hod_email_auth=hod_email, submission_department=user.department)
            notice_create.save()
            messages.info(request, "Notice Created Sucessfully")
            notices = notice.objects.filter(faculty_email_auth=request.user.email, user_who_created_notice=request.user.first_name)
            return render(request, "faculty/create_notice.html", {'notices': notices})
    else:
        data = notice.objects.filter(faculty_email_auth=request.user.email)
        print(notice)
        for i in data:
            print(i.note_title)
        return render(request, "faculty/create_notice.html", {'data': data})


def delete_note(request):
    id = request.GET['id']
    data1 = notice.objects.filter(id=id)
    data1.delete()
    data = notice.objects.filter(faculty_email_auth=request.user.email)
    print(notice)
    for i in data:
        print(i.note_title)
    return render(request, "faculty/create_notice.html", {'data': data})


def view_history(request):
    if request.method == 'POST':
        return HttpResponse("This is in POST method")
    else:
        print('This is GET')
        student_info = student.objects.filter(faculty_email=request.user.email)
        return render(request, "faculty/view_history.html", {"student_info":student_info})


def project_history(request):
    data = work_histort.objects.filter(group=request.GET['group'], semister=request.GET['sem'],faculty_email=request.user.email )
    print(data)
    return render(request, "faculty/work_chat_history.html", {"data": data})


def evaluate_student(request):
    event_id = evaltation_generate.objects.filter(id=request.GET['id'])
    title=''
    sem=0
    faculty_email_auth=''
    submission_date=''
    for i in event_id:
        title = i.submission_title
        sem = i.for_semister
        faculty_email_auth = i.faculty_email_auth

    student_data = student.objects.filter(faculty_email=faculty_email_auth, semister=sem)
    student_submit = event_submission.objects.filter(event_id=request.GET['id'], faculty_email_auth=request.user.email)
    for i in student_submit:
        submission_date = i.submission_last_date
        print(i.submission_date)
    # event_id = evaltation_generate.objects.filter(id = request.GET['id'])

    print(student_data)
    return render(request, "faculty/evaluation_table.html", {'student_submit':student_submit, 'event_id':event_id, 'title':title, 'sem':sem, 'faculty_email_auth':faculty_email_auth, 'student_data':student_data})


def student_marks(request):
    if request.method == 'POST':
        # test =
        a = request.POST['submission_id']
        b = request.POST['submit_marks']
        data = event_submission.objects.get(id = a)
        data.student_marks = b
        data.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        # print(student_data)
        # return render(request, "faculty/evaluation_table.html",
        #               {'student_submit': student_submit, 'event_id': event_id, 'title': title, 'sem': sem,
        #                'faculty_email_auth': faculty_email_auth, 'student_data': student_data})








