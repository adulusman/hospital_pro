from django import forms
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booking_date': DateInput(),
            'dob': DateInput(),
        }
        labels = {
            'p_name': 'Patient Name',
            'dob': 'Date of Birth',
            'phn': 'Phone',
            'email': 'Email',
            'gender': 'Gender',
            'department':'Departments',
            'doctor':'Doctors',
            'blood_group': 'Blood Group',
            'address': 'Address',
            'district': 'District',
            'sub_branch':'Sub Branch',
            'booking_date': 'Appointment Date',
        }


