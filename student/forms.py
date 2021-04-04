from django import forms

from student.models import event_submission, project_code, work_histort


class SubmissionForm(forms.ModelForm):
    class Meta:
        try:
            model = event_submission
            fields = [
                "student_id",
                "submission_file",
                "event_id",
                "submission_title",
                'for_semister',
                'student_name',
                'total_marks',
                'faculty_email_auth',
                'hod_email_auth',
                # 'submission_department'
                ]
        except Exception as ex:
            print(f"Exception is {ex}")


class workForm(forms.ModelForm):
    class Meta:
        model = work_histort
        fields = [
            "title",
            "discription",
            "student_id",
            "student_name",
        ]


class codeForm(forms.ModelForm):
    class Meta:
        model = project_code
        fields = [
            "project_code_file",
            "submition_status",
            "student_id",
            "group_name",
            "semister",
            "student_submited_code",
        ]

