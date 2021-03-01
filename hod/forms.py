from django import forms
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
                "hod_verification",
                "user_type",
                "college_url",
            ]
        except Exception as e:
            print(f"Exception occur is {e}")
        print("\n\n\n\n\nIn form")


class clg_detail(forms.ModelForm):
    class Meta:
        try:
            print("\n\n\n\n\nstarting form")
            model = college_details
            fields = [
                "college_name",
                "college_url",
                "college_email",
                "college_phone_number",
                "college_department_name",
            ]
        except Exception as e:
            print(f"\n\n\n\n\nException occur is {e}")
        print("\n\n\n\n\nIn form")


class testForm(forms.ModelForm):
    class Meta:
        model = test
        fields = ['image']
