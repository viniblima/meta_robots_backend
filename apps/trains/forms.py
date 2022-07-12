from django import forms
from .models import Train


class TrainForm(forms.ModelForm):

    class Meta:
        model = Train
        fields = '__all__'
