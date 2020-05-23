from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class ProfileForm(ModelForm):
	class Meta:
		model = Patient
		fields = '__all__'
		exclude = ['user','outstanding','paid','case_paper']

	def __init__(self, *args, **kwargs):
		super(ProfileForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
		self.fields['address'].widget.attrs['style'] = 'width:400px; height:40px; margin-top:10px; margin-bottom:10px'
		self.fields['name'].widget.attrs['style']  = 'width:250px; height:40px;margin-top:10px; margin-bottom:10px'
		self.fields['email'].widget.attrs['style']  = 'width:250px; height:40px;margin-top:10px; margin-bottom:10px'

class MedicalForm(ModelForm):
		class Meta:
			model = Medical
			fields = '__all__'
			exclude = ['invoice','payment','docname','Outstanding','date','total_amt']


class PatientForm(ModelForm):
	class Meta:
		model = Patient
		fields = '__all__'
		exclude = ['user']

	def __init__(self, *args, **kwargs):
		super(PatientForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
		self.fields['address'].widget.attrs['style'] = 'width:400px; height:40px; margin-top:10px; margin-bottom:10px'
		self.fields['name'].widget.attrs['style']  = 'width:250px; height:40px;margin-top:10px; margin-bottom:10px'
		self.fields['email'].widget.attrs['style']  = 'width:300px; height:40px;margin-top:10px; margin-bottom:10px'


class AppointmentForm(ModelForm):
	class Meta:
		model = Appointment
		fields = '__all__'
		widgets = {
            'date': forms.DateInput(attrs={'class':'datepicker'}),
        }

class DocForm(ModelForm):
	class Meta:
		model = Doctor
		fields = '__all__'
		exclude=['user','date_avail','time_avail','salary','attendance']
	def __init__(self, *args, **kwargs):
		super(DocForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
		self.fields['address'].widget.attrs['style'] = 'width:400px; height:40px; margin-top:10px; margin-bottom:10px'
		self.fields['name'].widget.attrs['style']  = 'width:250px; height:40px;margin-top:10px; margin-bottom:10px'
		self.fields['email'].widget.attrs['style']  = 'width:300px; height:40px;margin-top:10px; margin-bottom:10px'

class DoctorForm(ModelForm):
	class Meta:
		model = Doctor
		fields = '__all__'
		exclude=['user','date_avail','time_avail']
	def __init__(self, *args, **kwargs):
		super(DoctorForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
		self.fields['address'].widget.attrs['style'] = 'width:400px; height:40px; margin-top:10px; margin-bottom:10px'
		self.fields['name'].widget.attrs['style']  = 'width:250px; height:40px;margin-top:10px; margin-bottom:10px'
		self.fields['email'].widget.attrs['style']  = 'width:300px; height:40px;margin-top:10px; margin-bottom:10px'