from django import forms
from .models import *


class HodForm(forms.ModelForm):
    class Meta:
        try:
            print("\n\n\n\n\nIn starting form")
            model = hod_registration
            fields = ["name",
                "password",
                "department",
                "college_url",
                "email",
                "phone_number",
                "id_card_image",
                "verification",
                "user_type"
                ]
        except Exception as e:
            print(f"Exception occur is {e}")

        print("\n\n\n\n\nIn form")
