from django import forms
from django.contrib.auth.models import User

from . import models


class PatientUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']  # noqa: RUF012
        widgets = {  # noqa: RUF012
        'password': forms.PasswordInput()
        }

class PatientForm(forms.ModelForm):
    
    class Meta:
        model=models.Patient
        fields=['age','bloodgroup','disease','address','doctorname','mobile','profile_pic']  # noqa: RUF012
