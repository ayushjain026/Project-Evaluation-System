from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from faculty.models import temp_csv, faculty, evaltation_generate,notice
from student.forms import SubmissionForm, codeForm, workForm
from student.models import student, event_submission, project_code, work_histort, student_subjects


def email_verify(request):
    print("In student ")
    aa = request.GET['id']
    bb = request.GET['gmail']
    print(aa, bb)
    student_data = student.objects.get(id=aa, student_email=bb)
    print(student_data)
    # print(user.hod_verification)

    print(f"\n\n\nHOD VERIFICATION =  {student_data.verification}")
    student_data.verification = True
    print(f"\n\n\nHOD VERIFICATION =  {student_data.verification}")

    student_data.save()
    # verified = "verified"
    messages.info(request, "Congratulations your email is verified Successful")
    return render(request, "index.html")


def dashboard(request):
    user_data = student.objects.get(student_email=request.user.email)
    event_data = evaltation_generate.objects.filter(faculty_email_auth=user_data.faculty_email, for_semister=user_data.semister)
    return render(request, "student/dashboard.html", {'event_data':event_data})


def submission(request):
    if request.method == 'POST':
        id = request.POST["event_id"]
        get_event = evaltation_generate.objects.get(id=id)
        a = request.POST["student_id"]
        print(f"Id is ({id}), ({a})")
        form = SubmissionForm(request.POST, request.FILES)
        data1 = student.objects.get(student_email=request.user.email)
        print(form.is_valid())
        if event_submission.objects.filter(event_id=id, student_id=request.user.id):
            messages.info(request,"You can submit only once please contact your faculty")
            user_data = student.objects.get(student_email=request.user.email)
            event_data = evaltation_generate.objects.filter(faculty_email_auth=user_data.faculty_email, for_semister=user_data.semister)
            return render(request, "student/dashboard.html", {'event_data': event_data})
        else:
            print("in else")
            try:
                form = SubmissionForm(request.POST, request.FILES)
                if form.is_valid():
                    form.save()
                    data = event_submission.objects.get(student_id=request.user.id, event_id=id)
                    data.submission_status = True
                    data.submission_department = data1.department
                    data.submission_last_date = get_event.submission_last_date
                    if request.POST["submission_comment_student"]:
                        data.submission_comment_student = request.POST["submission_comment_student"]
                    data.save()
                    messages.info(request, "Documents Submited Sucessfully")
                    user_data = student.objects.get(student_email=request.user.email)
                    event_data = evaltation_generate.objects.filter(faculty_email_auth=user_data.faculty_email,for_semister=user_data.semister)
                    return render(request, "student/dashboard.html", {'event_data': event_data})
            except:
                messages.info(request, "You have already submited your assignment\nPlease contact your faculty in cause you have some query")
                user_data = student.objects.get(student_email=request.user.email)
                event_data = evaltation_generate.objects.filter(faculty_email_auth=user_data.faculty_email,
                                                                for_semister=user_data.semister)
                return render(request, "student/dashboard.html", {'event_data': event_data})
    else:
        id = request.GET["event_id"]
        print(id)
        event_into = evaltation_generate.objects.filter(id=id)
        print("\n\n\n\n\n\n",event_into)
        for i in event_into:
            print(i.id, i.submission_title)
        try:
            print(id, request.user.id)
            check = event_submission.objects.get(event_id=id, student_id=request.user.id)
            submission_status = check.submission_status
            print(submission_status)
        except Exception as ex:
            print("\n\n\n\n",ex)
            submission_status = False
        return render(request, "student/submission.html", {"event_into":event_into, "submission_status":submission_status})
# return render(request, "student/submission.html")


def project(request):
    if request.method=='POST':
        form = codeForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            messages.info(request, "Your Project is Uploaded for Evaluation 👍")
        return redirect('/')
    else:
        group=''
        sem=0
        p_c_d_name=''
        student_project = student.objects.filter(student_email=request.user.email)
        for i in student_project:
            group = i.group
            sem = i.semister
        if group == 'none':
            if project_code.objects.filter(student_id=request.user.id):
                project_codes = project_code.objects.get(student_id=request.user.id)
                p_c_d = True
                p_c_d_name = project_codes.student_submited_code
            else:
                p_c_d=False
                p_c_d_name='none'
            return render(request, "student/project.html", {"student_project": student_project, "p_c_d":p_c_d, 'p_c_d_name':p_c_d_name})
        else:
            p_c_d = ''
            submition_status=''
            student_submited_code=''
            print(sem, group)
            project_code_submission = project_code.objects.filter(semister=sem, group_name=group)
            print(project_code_submission)
            # if project_code.objects.filter(semister=sem, group_name=group):
            #     p_c_d = False
            #     print(p_c_d)
            # else:
            #     for i in project_code_submission:
            #         submition_status = i.submition_status
            #         student_submited_code = i.student_submited_code
            print("test")
            print(submition_status, student_submited_code)
            # p_c_d = submition_status
            p_c_d_name = student_submited_code
            if project_code.objects.filter(semister=sem, group_name=group):
                for i in project_code_submission:
                    p_c_d = i.submition_status
                    p_c_d_name = i.student_submited_code
            else:
                p_c_d = False
                print(p_c_d)
            grp_partner = student.objects.filter(group=group,semister=sem)
            return render(request, "student/project.html", {"student_project":student_project, "grp_partner":grp_partner, "p_c_d":p_c_d, "p_c_d_name":p_c_d_name})


def work_history(request):
    # return HttpResponse("Completed")
    student_data = student.objects.get(student_email=request.user.email)
    if request.method == 'POST':
        form = workForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            data = work_histort.objects.get(title=request.POST['title'], student_id=request.user.id, student_name=request.user.first_name)
            data.group = student_data.group
            data.semister = student_data.semister
            data.faculty_email = student_data.faculty_email
            data.save()
            messages.info(request, "Work History Created")
        student_data = student.objects.get(student_email=request.user.email)
        data = work_histort.objects.filter(group=student_data.group, semister=student_data.semister)
        return render(request, "student/work.html", {"data": data})
    else:
        student_data = student.objects.get(student_email=request.user.email)
        data = work_histort.objects.filter(group=student_data.group, semister=student_data.semister)
        return render(request, "student/work.html", {"data":data})


def profile(request):
    if request.method == "POST":
        user_info = student.objects.filter(student_email=request.POST['stu_email'])
        id = request.POST['id']
        data = student.objects.get(id=id)
        data.fullname = request.POST['stu_fname']
        # data.username = request.POST['fac_uname']
        # data.email = request.POST['fac_email']
        data.project_defination = request.POST['stu_Proj_def']
        data.hod_password = request.POST["stu_pass"]
        data1 = User.objects.get(username=request.user.username)
        data1.first_name = request.POST['stu_fname']
        # data1.email = request.POST["fac_email"]
        data1.username = request.POST["stu_email"]
        temp_pass = str(request.POST["stu_pass"])
        print(temp_pass, type(len(temp_pass)))
        print(len(temp_pass) == 2, len(temp_pass) == 1, len(temp_pass) == 0)
        check = 0
        if len(temp_pass) != 0 and len(temp_pass) >= 3:
            print(temp_pass, type(temp_pass))
            data1.set_password(temp_pass)
            update_session_auth_hash(request, data1)
            print("password saved")
            check = 1
            # return render(request, 'profile.html', {'user_info': user_info})
        if len(temp_pass) == 2 or len(temp_pass) == 1:
            print("here in too small")
            messages.info(request, 'Password is too small try again with different password')
        data.save()
        data1.save()
        dep = []
        for user in user_info:
            print(user.subjects)
            dep.append(user.subjects)
        if check == 1:
            messages.info(request, "Data saved SucessFully")
        else:
            messages.info(request, "All the fields are saved without Password")
        user_info = student.objects.filter(student_email=request.user.email)
        a = user_info[0].id
        user_info = student.objects.filter(id=a)
        sub = student_subjects.objects.filter(student_id=request.user.email)
        return render(request, "faculty/profile.html", {"user_info": user_info, "sub":sub})
    else:
        email = request.GET['email']
        user_info = student.objects.filter(student_email=email)
        print(user_info)
        dep = []
        for user in user_info:
            print(user.subjects)
            dep.append(user.subjects)
        print(dep)

        print(user_info[0].id, type(user_info))
        a = user_info[0].id
        user_info = student.objects.filter(id=a)
        sub = student_subjects.objects.filter(student_id=request.user.email)
        for i in sub:
            print(i.subject)
        return render(request, "student/profile.html", {"user_info": user_info, "sub":sub})


def notices(request):
    fac = student.objects.get(student_email=request.user.email)
    print(fac.faculty_email, fac.semister)
    try:
        if notice.objects.filter(faculty_email_auth=fac.faculty_email, for_semister=fac.semister):
            print("in if block")
            data = notice.objects.filter(faculty_email_auth=fac.faculty_email, for_semister=int(fac.semister))
            print(data)
            return render(request, "student/notice.html", {'data': data})
        else:
            print("in else block")
            return render(request, "student/notice.html")
    except Exception as e:
        print(" in exception ",e)
        return render(request, "student/notice.html")
