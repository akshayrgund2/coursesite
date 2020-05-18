from django import forms

# import GeeksModel from models.py
from .models import Student , course_enrolment


# create a ModelForm
class StudentForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Student
        fields = "__all__"

class EnrollForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = course_enrolment
        fields = "__all__"

