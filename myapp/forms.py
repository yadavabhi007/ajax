from django import forms
from .models import User
gender_choices = (("Male","Male"), ("Female","Female"))

class StudentRegistration(forms.ModelForm):
    gender = forms.ChoiceField(choices=gender_choices,widget=forms.RadioSelect())
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(render_value = True),
        }