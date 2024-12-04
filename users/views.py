from django.shortcuts import render, redirect
from .forms import RegisterForm
from users.forms import Prediction_form

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile

from django.urls import reverse
# users/views.py
from django.shortcuts import render

def result(request):
    # Your logic for the result view
    return render(request, 'result.html')





def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            phone_number=form.cleaned_data.get('phone_number')
            dob=form.cleaned_data.get('dob')
            Hospital_name=form.cleaned_data.get('Hospital_name')
            profile=UserProfile(user=user,phone_number=phone_number,dob=dob)
            profile.save()
            login(request, user)
            return redirect('successfully_registered')
        
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

def successfully_registered(request):
    return render(request, 'users/successfully_registered.html')

def login_view(request):  #dont name "login" bcoz django already have build-in log in function"
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('successfully_logged_in')  # Redirect successful login
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

@login_required  # Ensure the user is logged in before accessing this view
def successfully_logged_in(request):
    return render(request, 'users/successfully_logged_in.html')


def result(request):
    return render(request, 'users/result.html')

import numpy as np
import pandas as pd
import joblib
model=joblib.load('./knn_model.pkl')
   
def prediction_form(request):
    if request.method == 'POST':
        form = Prediction_form(data=request.POST)
        if form.is_valid():
            Height_cm = form.cleaned_data.get('height')
            Weight_kg = form.cleaned_data.get('weight')
            Temperature_C = form.cleaned_data.get('temperature')
            Heart_Rate = form.cleaned_data.get('heart_rate')
            Symptoms = form.cleaned_data.get('symptoms')
            Existing_Conditions = form.cleaned_data.get('existing_conditions')
            Laboratory_Test_Results = form.cleaned_data.get('laboratory_results')
            Cholesterol_mg_dL = form.cleaned_data.get('cholesterol')
            Blood_Sugar_mg_dL = form.cleaned_data.get('blood_sugar')
            Family_History_Heart_Disease = form.cleaned_data.get('family_history')
            Smoking_Status = form.cleaned_data.get('smoking_status')
            Blood_Pressure_Systolic = form.cleaned_data.get('systolic')
            Blood_Pressure_Diastolic = form.cleaned_data.get('diastolic')
           
            features_after_onehotencoding =['Height_cm', 'Weight_kg', 'Temperature_C', 'Heart_Rate',
            'Cholesterol_mg_dL', 'Blood_Sugar_mg_dL', 'Blood_Pressure_Systolic',
            'Blood_Pressure_Diastolic', 'Symptoms_dizziness', 'Symptoms_fatigue',
            'Symptoms_nausea', 'Symptoms_palpitations','Symptoms_shortness of breath', 'Existing_Conditions_Diabetes',
            'Existing_Conditions_High Cholesterol',
            'Existing_Conditions_Hypertension',
            'Laboratory_Test_Results_High Cholesterol',
            'Laboratory_Test_Results_Low Iron', 'Laboratory_Test_Results_Normal',
            'Family_History_Heart_Disease_Yes', 'Smoking_Status_Former',
            'Smoking_Status_Never']

            input_data = {col: 0 for col in features_after_onehotencoding} 

            if 'chest pain' in Symptoms:
                input_data['Symptoms_chest pain'] = 1
            if 'shortness of breath' in Symptoms:
                input_data['Symptoms_shortness of breath'] = 1
            if 'dizziness' in Symptoms:
                input_data['Symptoms_dizziness'] = 1
            if 'fatigue' in Symptoms:
                input_data['Symptoms_fatigue'] = 1


            if 'diabetes' in Existing_Conditions:
                input_data['Existing_Conditions_Diabetes'] = 1
            if 'high cholesterol' in Existing_Conditions:
                input_data['Existing_Conditions_High Cholesterol'] = 1
            if 'hypertension' in Existing_Conditions:
                input_data['Existing_Conditions_Hypertension'] = 1
            if 'asthma' in Existing_Conditions:
                input_data['Existing_Conditions_Asthma'] = 1


            if 'high cholesterol' in Laboratory_Test_Results:
                input_data['Laboratory_Test_Results_High Cholesterol'] = 1
            if 'low iron' in Laboratory_Test_Results:
                input_data['Laboratory_Test_Results_Low Iron'] = 1
            if 'normal' in Laboratory_Test_Results:
                input_data['Laboratory_Test_Results_Normal'] = 1
           
            if 'yes' in Family_History_Heart_Disease:
                input_data['Family_History_Heart_Disease_Yes'] = 1
            else:
                input_data['Family_History_Heart_Disease_No'] = 1


            if 'former' in Smoking_Status:
                input_data['Smoking_Status_Former'] = 1
            if 'never' in Smoking_Status:
                input_data['Smoking_Status_Never'] = 1
            
            input_data['Height_cm'] = Height_cm
            input_data['Weight_kg'] = Weight_kg
            input_data['Temperature_C'] = Temperature_C
            input_data['Heart_Rate'] = Heart_Rate
            input_data['Cholesterol_mg_dL'] = Cholesterol_mg_dL
            input_data['Blood_Sugar_mg_dL'] = Blood_Sugar_mg_dL
            input_data['Blood_Pressure_Systolic'] = Blood_Pressure_Systolic
            input_data['Blood_Pressure_Diastolic'] = Blood_Pressure_Diastolic

            input_data = pd.DataFrame([input_data])

            for col in features_after_onehotencoding:
                if col not in input_data:
                    input_data[col] = 0

            input_data = input_data[features_after_onehotencoding]  
       
            prediction = model.predict(input_data)
            

           
            return render(request, 'users/result.html', {
                'prediction': prediction 
            })
        
        
    else:
        form = Prediction_form()
    return render(request, 'users/prediction_form.html', {'form': form})



