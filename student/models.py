from django.db import models


class student(models.Model):
    fullname = models.CharField(max_length=50,null=True)
    username = models.CharField(max_length=50,null=True)
    password = models.CharField(max_length=60,null=True)
    college_name = models.CharField(max_length=50, default='abc',null=True)
    student_email = models.EmailField(default='abc@gmail.com',null=True)
    subjects = models.CharField(max_length=50,null=True)
    group = models.CharField(max_length=100, null=True)
    semister = models.IntegerField(null=True)
    project_defination = models.CharField(max_length=3000, null=True)
    user_type = models.IntegerField(null=True)
    verification = models.BooleanField()
    hod_email = models.EmailField(null=True)
    faculty_email = models.EmailField(null=True)
    department = models.CharField(max_length=100, default='abc',null=True)


class temp_csv_for_students(models.Model):
    csv_file = models.FileField(upload_to='temp/documents/')
    sem = models.CharField(max_length=60, null=True)
    faculty_name = models.EmailField(default='abc@gmail.com')


class event_submission(models.Model):
    student_id = models.IntegerField(null=True)
    student_name = models.CharField(max_length=100)
    event_id = models.IntegerField(null=True)
    submission_status = models.BooleanField(default=False)
    submission_title = models.CharField(max_length=250, null=True)
    for_semister = models.IntegerField(null=True)
    submission_date = models.DateTimeField(auto_now_add=True, null=True)
    submission_last_date = models.DateTimeField(null=True)
    submission_file = models.FileField(upload_to='student_doc/')
    student_marks = models.IntegerField(null=True)
    total_marks = models.IntegerField()
    submission_comment_student = models.CharField(max_length=2000, null=True, default="none")
    faculty_email_auth = models.EmailField(null=True)
    hod_email_auth = models.EmailField(null=True)
    submission_department = models.CharField(max_length=100, null=True)


class project_code(models.Model):
    project_code_file = models.FileField(upload_to='Project_Code')
    submition_status = models.BooleanField(null=True)
    student_id = models.IntegerField(null=True)
    group_name = models.CharField(max_length=400)
    semister = models.IntegerField(null=True)
    student_submited_code = models.CharField(max_length=100, null=True)


class work_histort(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    discription = models.CharField(max_length=700)
    student_id = models.IntegerField()
    student_name = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    semister = models.IntegerField(null=True)
    faculty_email = models.EmailField(null=True)


class student_subjects(models.Model):
    subject = models.CharField(max_length=100)
    faculty = models.EmailField()
    student_id = models.EmailField()
    hod = models.EmailField()


