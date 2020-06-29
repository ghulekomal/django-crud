from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('Fullname', 'Emp_code', 'Mobile', 'Position')
        labels = {'Fullname': 'FullName',
        'Emp_code':'EMP .Code'}

def __init__(self, *args, **kwargs):
    super(EmployeeForm, self).__init__(*args, **kwargs)
    #self.fields['position'].empty_label = "Select"
    self.fields['Position'].required = False
    self.fields['Emp_code'].required = False