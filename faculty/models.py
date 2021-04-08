from django.db import models
from django.utils import timezone


class faculty(models.Model):
    fullname = models.CharField(max_length=50,null=True)
    username = models.CharField(max_length=50,null=True)
    password = models.CharField(max_length=60,null=True)
    college_name = models.CharField(max_length=50, default='abc',null=True)
    faculty_email = models.EmailField(default='abc@gmail.com',null=True)
    subjects = models.CharField(max_length=50,null=True)
    user_type = models.IntegerField(null=True)
    verification = models.BooleanField()
    hod_email = models.EmailField(null=True)
    department = models.CharField(max_length=100, default='abc',null=True)


class temp_csv(models.Model):
    csv_file = models.FileField(upload_to='temp/documents/')
    department = models.CharField(max_length=60, null=True)
    hod_name = models.EmailField(default='abc@gmail.com')


# class evaluation(models.Model):
#     submission_title = models.CharField(max_length=250, null=True)
#     for_semister = models.IntegerField()
#     submission_date = models.DateTimeField()
#     submission_last_date = models.DateTimeField()
#     submission_status = models.BooleanField()
#     submission_file_title = models.CharField(max_length=2000, null=True)
#     submission_file = models.FileField(upload_to='temp/submission')
#     submission_comment_faculty = models.CharField(max_length=2000, null=True)
#     submission_comment_student = models.CharField(max_length=2000, null=True)
#     students_submission_email = models.EmailField(null=True)
#     faculty_email_auth = models.EmailField()
#     hod_email_auth = models.EmailField()
#     submission_marks = models.IntegerField()
#     submission_department = models.CharField(max_length=100, null=True)


class evaltation_generate(models.Model):
    submission_title = models.CharField(max_length=250, null=True)
    for_semister = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    submission_last_date = models.DateTimeField()
    submission_file_description = models.CharField(max_length=2000, null=True)
    submission_comment_faculty = models.CharField(max_length=2000, null=True, default="none")
    submission_marks = models.IntegerField()
    total_marks = models.IntegerField(null=True)
    faculty_email_auth = models.EmailField()
    hod_email_auth = models.EmailField()
    submission_department = models.CharField(max_length=100, null=True)


class notice(models.Model):
    note_title = models.CharField(max_length=250, null=True)
    note_description = models.CharField(max_length=5000)
    for_semister = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    faculty_email_auth = models.EmailField()
    user_who_created_notice = models.CharField(max_length=100)
    hod_email_auth = models.EmailField()
    submission_department = models.CharField(max_length=100, null=True)