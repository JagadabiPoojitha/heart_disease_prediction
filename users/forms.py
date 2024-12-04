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


class Prediction_form(forms.Form):
    height = forms.FloatField(
        label='Height (cm)',
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        required=True
    )
    weight = forms.FloatField(
        label='weight (kg)',
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        required=True
    )
    temperature = forms.FloatField(
        label='Temperature (°C)',
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        required=True
    )
    heart_rate = forms.FloatField(
        label='heart_rate (bpm)',
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        required=True
    )
    cholesterol = forms.FloatField(
        label='cholesterol (mg/dl)',
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        required=True
    )
    blood_sugar = forms.FloatField(
        label='blood_sugar (mg/dl)',
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        required=True
    )
    systolic = forms.FloatField(
        label='Systolic Pressure',
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        required=True
    )
    diastolic = forms.FloatField(
        label='Diastolic Pressure',
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        required=True
    )
    symptoms = forms.ChoiceField(
        choices=[
            ('None', 'None'),
            ('Chest Pain', 'Chest Pain'),
            ('Shortness of Breath', 'Shortness of Breath'),
            ('Dizziness', 'Dizziness'),
            ('Fatigue', 'Fatigue')
            
        ],
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )
    existing_conditions = forms.ChoiceField(
        choices=[
            ('None', 'None'),
            ('Diabetes', 'Diabetes'),
            ('Hypertension', 'Hypertension'),
            ('High Cholesterol', 'High Cholesterol'),
            ('Asthma', 'Asthma')
            
        ],
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )
    family_history = forms.ChoiceField(
        choices=[
            ('No', 'No'),
            ('Yes', 'Yes')
            
        ],
        label='Family History of Heart Disease',
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )
    laboratory_results = forms.ChoiceField(
        choices=[
            ('Normal', 'Normal'),
            ('High Cholesterol', 'High Cholesterol'),
            ('Low Iron', 'Low Iron'),
            ('High Blood Sugar', 'High Blood Sugar')    
        ],
        label='Laboratory Results',
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )
    smoking_status = forms.ChoiceField(
        choices=[
            ('Never', 'Never'),
            ('Former', 'Former'),
            ('Current', 'Current')
        ],
        label='Smoking Status',
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )        