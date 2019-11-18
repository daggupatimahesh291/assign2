from django import forms  
from note.models import note
class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = note
        fields = "__all__"  
