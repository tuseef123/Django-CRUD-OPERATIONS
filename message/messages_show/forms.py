from django.forms import ModelForm
from .models import Profile

class AddData(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'