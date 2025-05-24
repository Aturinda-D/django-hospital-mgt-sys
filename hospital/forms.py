from django.forms import ModelForm, TextInput, DateInput, DateTimeInput, Select
from .models import Patient, Appointment

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ["name", "date_of_birth", "phone_number"]
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Full name'}),
            'date_of_birth': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'phone_number': TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}),
        }


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ["patient", "appointment_date", "reason"]
        widgets = {
            'patient': Select(attrs={'class': 'form-control', 'placeholder': 'Choose patient'}),
            'appointment_date': DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'reason': TextInput(attrs={'class': 'form-control', 'placeholder': 'Reason for appointment'})
        }
