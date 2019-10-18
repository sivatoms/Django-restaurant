from django import forms
from .models import Reservation
from datetime import datetime

class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['LastName', 'FirstName', 'NumberOfGuests', 'ReserveDate', 'Time']
        widgets = {
           'ReserveDate':DateInput(),
           'Time':TimeInput(),
        }

    