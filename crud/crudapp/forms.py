from crudapp.models import record
from django import forms
class colform(forms.ModelForm):
    class Meta:
        model = record
        fields= '__all__'