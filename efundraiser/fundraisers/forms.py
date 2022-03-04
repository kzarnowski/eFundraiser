from django import forms
from .models import Fundraiser
from django.forms import ModelForm

class DateInput(forms.DateTimeInput):
    input_type = 'date'

class FundraiserForm(ModelForm):
    class Meta:
        model = Fundraiser
        fields = [
            'title',
            'description',
            'end_time',
            'amount_to_raise'
        ]
        widgets = {
            'end_time': DateInput()
        }
    # title = forms.CharField(max_length=20)
    # description = forms.CharField(widget=forms.Textarea, max_length=2000)
    # end_time = forms.DateTimeField()
    # amount_to_raise = forms.FloatField()

