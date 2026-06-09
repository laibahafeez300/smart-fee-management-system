from django import forms
from .models import StudentFee

class StudentFeeForm(forms.ModelForm):

    class Meta:
        model = StudentFee
        fields = '__all__'