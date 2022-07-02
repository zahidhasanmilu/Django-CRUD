from django import forms
from django.forms import ModelForm
from .models import Student


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('name','student_id', 'department', 'section','semester', 'phone')
        
        widgets ={
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'student_id' : forms.TextInput(attrs={'class':'form-control'}),
            'department' : forms.Select(attrs={'class':'form-control'}),
            'section' : forms.Select(attrs={'class':'form-control'}),
            'semester' : forms.Select(attrs={'class':'form-control'}),
            'phone' : forms.TextInput(attrs={'class':'form-control'}),
        }