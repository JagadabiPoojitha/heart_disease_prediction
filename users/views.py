from django.shortcuts import render, redirect,get_object_or_404
from .forms import RegisterForm
import csv,pickle,random
import numpy as np
from django.http import HttpResponse
from users.forms import Prediction_form

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile,HealthTip  # Replace `your_app` with the name of your app

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from .models import HealthTip
from django.http import JsonResponse
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import io
import base64
from django.http import HttpResponse
import random  # Simulate prediction for demonstration

from django.urls import reverse
from datetime import datetime
from .models import PredictionHistory


def result(request):
    # Your logic for the result view
    return render(request, 'result.html')





def home(request):
    return render(request, 'home.html')



from django.shortcuts import render, redirect
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Process registration logic here
            # e.g., save user to the database
            return redirect('login')
    else:
        form = RegistrationForm()

    # Render the form with the CSRF token by passing the request
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

# users/views.py



def dashboard(request):
    # Render the correct path
    return render(request, 'users/dashboard.html', {})





def load_models():
    try:
        model = joblib.load(r'C:\Users\EliteBook\Desktop\HDP\knn_model.pkl')
        scaler = joblib.load(r'C:\Users\EliteBook\Desktop\HDP\scaler.pkl')
        one_hot_encoder = joblib.load(r'C:\Users\EliteBook\Desktop\HDP\encoder.pkl')
        label_encoder = joblib.load(r'C:\Users\EliteBook\Desktop\HDP\label_encoder.pkl')
        return model, scaler, one_hot_encoder, label_encoder
    except Exception as e:
        print(f"Error loading models: {e}")
        return None, None, None, None
   
def prediction_form(request):
        model, scaler, one_hot_encoder, label_encoder = load_models()
    
        if not model:
            return JsonResponse({'error': 'Model loading failed'}, status=500)
    
        if request.method == 'POST':
            form = Prediction_form(request.POST)
            if form.is_valid():
            # Capture the form data
                height = form.cleaned_data['height']
                weight = form.cleaned_data['weight']
                temperature = form.cleaned_data['temperature']
                heart_rate = form.cleaned_data['heart_rate']
                cholestrol = form.cleaned_data['cholestrol']
                blood_sugar = form.cleaned_data['blood_sugar']
                systolic = form.cleaned_data['systolic']
                diastolic = form.cleaned_data['diastolic']
                existing_conditions = form.cleaned_data['existing_conditions']
                family_history = form.cleaned_data['family_history']
                smoking_status = form.cleaned_data['smoking_status']
                lab_status = form.cleaned_data['lab_status']
                symptoms = form.cleaned_data['symptom']
            
                categorical_columns = [
                    'Symptoms_chest pain', 'Symptoms_dizziness', 'Symptoms_fatigue', 
                    'Symptoms_nausea', 'Symptoms_palpitations', 'Symptoms_shortness of breath',
                    'Existing_Conditions_Asthma', 'Existing_Conditions_Diabetes', 
                    'Existing_Conditions_High Cholesterol', 'Existing_Conditions_Hypertension', 
                    'Existing_Conditions_Thyroid', 'Laboratory_Test_Results_High Blood Sugar', 
                    'Laboratory_Test_Results_High Cholesterol', 'Laboratory_Test_Results_Low Iron', 
                    'Laboratory_Test_Results_Normal', 'Smoking_Status_Current', 
                    'Smoking_Status_Former', 'Smoking_Status_Never', 
                    'Family_History_Heart_Disease_No', 'Family_History_Heart_Disease_Yes'
                ]
            
                input_data = {col: [False] for col in categorical_columns}

                 # Setting the appropriate columns to True based on user selection
                if 'chest pain' in symptoms:
                    input_data['Symptoms_chest pain'] = [True]
                if 'dizziness' in symptoms:
                    input_data['Symptoms_dizziness'] = [True]
                if 'fatigue' in symptoms:
                    input_data['Symptoms_fatigue'] = [True]
                if 'nausea' in symptoms:
                    input_data['Symptoms_nausea'] = [True]
                if 'palpitations' in symptoms:
                    input_data['Symptoms_palpitations'] = [True]
                if 'shortness of breath' in symptoms:
                    input_data['Symptoms_shortness of breath'] = [True]
            
                if 'Asthma' in existing_conditions:
                    input_data['Existing_Conditions_Asthma'] = [True]
                if 'Diabetes' in existing_conditions:
                    input_data['Existing_Conditions_Diabetes'] = [True]
                if 'High Cholesterol' in existing_conditions:
                    input_data['Existing_Conditions_High Cholesterol'] = [True]
                if 'Hypertension' in existing_conditions:
                    input_data['Existing_Conditions_Hypertension'] = [True]
                if 'Thyroid' in existing_conditions:
                    input_data['Existing_Conditions_Thyroid'] = [True]
            
                if 'High Blood Sugar' in lab_status:
                    input_data['Laboratory_Test_Results_High Blood Sugar'] = [True]
                if 'High Cholesterol' in lab_status:
                    input_data['Laboratory_Test_Results_High Cholesterol'] = [True]
                if 'Low Iron' in lab_status:
                    input_data['Laboratory_Test_Results_Low Iron'] = [True]
                if 'Normal' in lab_status:
                    input_data['Laboratory_Test_Results_Normal'] = [True]
            
                if smoking_status == 'Current':
                    input_data['Smoking_Status_Current'] = [True]
                if smoking_status == 'Former':
                    input_data['Smoking_Status_Former'] = [True]
                if smoking_status == 'Never':
                    input_data['Smoking_Status_Never'] = [True]
            
                if family_history == 'Yes':
                    input_data['Family_History_Heart_Disease_Yes'] = [True]
                else:
                    input_data['Family_History_Heart_Disease_No'] = [True]
            
                input_data['Height_cm'] = [height]
                input_data['Weight_kg'] = [weight]
                input_data['Temperature_C'] = [temperature]
                input_data['Heart_Rate'] = [heart_rate]
                input_data['Cholesterol_mg_dL'] = [cholestrol]
                input_data['Blood_Sugar_mg_dL'] = [blood_sugar]
                input_data['Systolic_BP'] = [systolic]
                input_data['Diastolic_BP'] = [diastolic]
            
                # Create DataFrame for the input data
                input_df = pd.DataFrame(input_data)
            
                # Define the columns order from the training data
                model_columns = [
                    'Height_cm', 'Weight_kg', 'Temperature_C', 'Heart_Rate'
                    ,'Cholesterol_mg_dL', 'Blood_Sugar_mg_dL', 
                    'Symptoms_chest pain', 'Symptoms_dizziness', 'Symptoms_fatigue', 
                    'Symptoms_nausea', 'Symptoms_palpitations', 'Symptoms_shortness of breath',
                    'Existing_Conditions_Asthma', 'Existing_Conditions_Diabetes', 
                    'Existing_Conditions_High Cholesterol', 'Existing_Conditions_Hypertension', 
                    'Existing_Conditions_Thyroid', 'Laboratory_Test_Results_High Blood Sugar', 
                    'Laboratory_Test_Results_High Cholesterol', 'Laboratory_Test_Results_Low Iron', 
                    'Laboratory_Test_Results_Normal', 'Smoking_Status_Current', 
                    'Smoking_Status_Former', 'Smoking_Status_Never', 
                    'Family_History_Heart_Disease_No', 'Family_History_Heart_Disease_Yes', 
                    'Systolic_BP', 'Diastolic_BP'
                ]
            
                for col in model_columns:
                    if col not in input_df.columns:
                        input_df[col] = 0  # Adding missing columns with value 0
            
                input_df = input_df[model_columns]

                # Make the prediction
                prediction = model.predict(input_df)
            
                # Get the disease name using label encoding 
                disease_name = label_encoder.inverse_transform(prediction)
            
                # Render the result page with the prediction
                return render(request, 'users/Prediction_form.html', {'prediction': disease_name[0]})
        
            else:
                return JsonResponse({'error': 'Invalid form input'}, status=400)
        else:
            form = Prediction_form()
            return render(request, 'users/Prediction_form.html', {'form': form})


# views.py


from django.shortcuts import render
from .models import HealthTip


def health_tips(request):
    # Fetch all tips related to 'heart_disease' category
    tips = HealthTip.objects.filter(category='heart_disease')
    # Pass the tips to the template
    return render(request, 'health_tips.html', {'tips': tips})


# Simulate prediction for demonstration

def predict(request):
    if request.method == "POST":
        # Simulate a risk percentage prediction result (replace with KNN model prediction logic)
        risk_percentage = random.randint(0, 100)

        # Redirect to visualization page
        request.session['risk_percentage'] = risk_percentage  # Store prediction result in session
        return redirect('results_chart')

    # Render the prediction form
    return render(request, 'predict.html')

  # Import here to avoid circular dependency


def results_chart(request):
    # Retrieve risk percentage from the session
    risk_percentage = request.session.get('risk_percentage', 0)

    # Create a pie chart or bar chart using Matplotlib
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.pie(
        [risk_percentage, 100 - risk_percentage],
        labels=[f"Risk: {risk_percentage}%", f"No Risk: {100 - risk_percentage}%"],
        colors=["red", "green"],
        autopct='%1.1f%%',
        startangle=90,
    )
    ax.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle.

    # Save the plot to BytesIO
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()

    # Render the results with the chart
    context = {"image_base64": image_base64, "risk_percentage": risk_percentage}
    return render(request, 'results.html', context)




def trend_analysis(request):
    # Fetch user prediction data from database
    predictions = PredictionHistory.objects.all().order_by('timestamp')
    dates = [p.timestamp.strftime('%Y-%m-%d') for p in predictions]
    risk_values = [p.risk_percentage for p in predictions]

    # Create Line Graph
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(dates, risk_values, marker='o')
    ax.set_xlabel('Date')
    ax.set_ylabel('Risk Percentage')
    ax.set_title('Heart Disease Risk Over Time')
    ax.grid()

    # Save the graph to BytesIO
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()

    context = {"image_base64": image_base64}
    return render(request, 'trend_analysis.html', context)
