from django import forms
from faculty.models import *
from student.models import temp_csv_for_students, project_code


class csvForm_faculty(forms.ModelForm):
    class Meta:
        try:
            model = temp_csv_for_students
            fields = ("csv_file",
                     "sem",
                     "faculty_name",
                      )
        except Exception as e:
            print(f"\n\n\n\n\nException occur is {e}")


class create_submission_form(forms.ModelForm):
    class Meta:
        model = evaltation_generate
        fields = ("submission_title",
                  "for_semister",
                  "submission_last_date",
                  "submission_file_description",
                  "submission_marks",
                  "faculty_email_auth",
                  )





