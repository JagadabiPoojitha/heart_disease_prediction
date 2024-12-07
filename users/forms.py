from django import forms 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 

class RegisterForm(UserCreationForm): 
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15,required=True)
    dob=forms.DateField(required=True,widget=forms.SelectDateWidget(years=range(1900,2024)))
    Hospital_name=forms.CharField(required=True,max_length=100)
    
    class Meta: 

        model = User
        fields = ['username', 'email', 'phone_number','dob','Hospital_name', 'password1', 'password2']

from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import re

# Custom password validation logic
def validate_password(password):
    # Rule 1: Password can't be too similar to other personal information.
    # This example assumes they shouldn't use their username, hospital name, or other similar terms.
    if re.search(r'username', password, re.IGNORECASE):
        raise ValidationError("Password is too similar to your username.")
    if re.search(r'hospital', password, re.IGNORECASE):
        raise ValidationError("Password is too similar to your hospital name.")

    # Rule 2: Password should be at least 8 characters
    if len(password) < 8:
        raise ValidationError("Your password must contain at least 8 characters.")

    # Rule 3: Password can't be entirely numeric
    if password.isnumeric():
        raise ValidationError("Your password cannot be entirely numeric.")

    # Rule 4: Password can't be a commonly used password
    commonly_used_passwords = ['123456', 'password', 'qwerty', 'abc123']
    if password.lower() in commonly_used_passwords:
        raise ValidationError("Your password can't be a commonly used password.")


class RegistrationForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Enter username"}),
        
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={"placeholder": "Enter email"})
    )
    phone_number = forms.CharField(
        required=True,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ],
        widget=forms.TextInput(attrs={"placeholder": "Enter phone number"})
    )
    dob = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={"type": "date"})
    )
    hospital_name = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Enter hospital name"})
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={"placeholder": "Enter password"}),
        
    )
    password_confirmation = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm password"})
    )

    # Custom clean method for validating password
    def clean_password(self):
        password = self.cleaned_data.get('password')
        validate_password(password)
        return password

    # Ensure that the password and its confirmation match
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirmation = cleaned_data.get('password_confirmation')

        if password and password_confirmation and password != password_confirmation:
            raise ValidationError("Passwords do not match.")

class Prediction_form(forms.Form):
     height = forms.FloatField(
        label='Height (cm)',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
        )
     weight = forms.FloatField(
        label='Weight (kg)',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
        )
     temperature = forms.FloatField(
        label='Temperature (C)',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
        )
     heart_rate = forms.FloatField(
        label='Heart_rate (C)',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
        )
     
     cholestrol = forms.FloatField(
        label='Cholestrol (mg/dl)',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
        )
     blood_sugar = forms.FloatField(
        label='Blood_Sugar  (mg/dl)',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
        )
     systolic = forms.FloatField(
        label='Systolic Pressure',
       widget=forms.NumberInput(attrs={'class': 'form-control'})
        )
     diastolic = forms.FloatField(
        label='Diastolic Pressure', widget=forms.NumberInput(attrs={'class': 'form-control'})
        )
     existing_conditions = forms.ChoiceField(
        choices=[
            ('Diabetes', 'Diabetes'),
            ('Hypertension', 'Hypertension'),
            ('High cholestrol', 'High cholestrol'),
            ('Asthma', 'Asthma'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
        )
     family_history = forms.ChoiceField(
        choices=[
            ('Yes', 'Yes'),
            ('No', 'No'),
        ],
        label='Family History of Heart Disease',
        widget=forms.Select(attrs={'class': 'form-control'})
        )
     smoking_status = forms.ChoiceField(
        choices=[
            ('Never', 'Never'),
            ('Former', 'Former'),
            ('Current', 'Current'),
    
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
        )
     lab_status = forms.ChoiceField(
        choices=[
            ('High Blood Sugar', 'High Blood Sugar'),
            ('High cholestrol', 'High cholestrol'),
            ('Low Iron', 'Low Iron'),
            ('Normal Test Results', 'Normal Test Results'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
        )
     symptom= forms.ChoiceField(
        choices=[
            ('chest pain', 'chest pain'),
            ('dizziness', 'dizziness'),
            ('fatigue', 'fatigue'),
            ('nausea', 'nausea'),
            ('palpitations', 'palpitations'),
            ('shortness of breath', 'shortness of breath'),

        ],
        widget=forms.Select(attrs={'class': 'form-control'})
        )

