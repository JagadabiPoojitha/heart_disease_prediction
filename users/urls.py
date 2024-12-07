from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include




urlpatterns = [
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('successfully_registered/', views.successfully_registered, name='successfully_registered'),
    path('successfully_logged_in/', views.successfully_logged_in, name='successfully_logged_in'),
    
    path('prediction_form/', views.prediction_form, name='prediction_form'),
    path('result/', views.result, name='result'),
    path('dashboard/', views.dashboard, name='dashboard'),
   
    
    
    
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='password/password_reset_form.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password/password_reset_complete.html'), name='password_reset_complete'),

    path('health-tips/', views.health_tips, name='health_tips'),

  
    path('predict/', views.predict, name="predict"),  # Handle predictions
    path('results/', views.results_chart, name="results_chart"),  # Results visualization

        
]
