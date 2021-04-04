from django import forms

from faculty.models import temp_csv
from .models import *


class HodForm(forms.ModelForm):
    class Meta:
        try:
            model = hod_registration
            fields = [
                "hod_fullname",
                "hod_username",
                "hod_password",
                "college_name",
                "college_department_name",
                "hod_email",
                "hod_phone_number",
                "hod_id_card_image",
                "verification",
                "user_type",
                "college_url",
            ]
        except Exception as e:
            print(f"Exception occur is {e}")


class clg_detail(forms.ModelForm):
    class Meta:
        try:
            model = college_details
            fields = [
                "college_name",
                "college_url",
                "college_email",
                "college_phone_number",
                "college_department_name",
            ]
        except Exception as e:
            print(f"Exception occur is {e}")



class testForm(forms.ModelForm):
    class Meta:
        model = test
        fields = ['image']


class csvForm(forms.ModelForm):
    class Meta:
        try:
            model = temp_csv
            fields = ("csv_file",
                     "department",
                     "hod_name",
                      )
        except Exception as e:
            print(f"\n\n\n\n\nException occur is {e}")


