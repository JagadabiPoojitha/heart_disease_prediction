from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    phone_number=models.CharField(max_length=15,blank=True, null=True)
    dob=models.DateField(null=True, blank=True)
    Hospital_name=models.CharField(blank=True,max_length=100)

    def __str__(self):
        return f"{self.user.username}'s profile"






from django.db import models


class HealthTip(models.Model):
    title = models.CharField(max_length=200)  # Tip title
    description = models.TextField()  # Tip description
    category = models.CharField(
        max_length=50,
        choices=[
            ('heart_disease', 'Heart Disease'),
            ('lifestyle', 'Lifestyle'),
            ('diet', 'Diet'),
            ('exercise', 'Exercise'),
        ],
    )  # Tip category (choice for better database integrity)

    def __str__(self):
        return self.title



from django.db import models

class PredictionHistory(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    risk_percentage = models.IntegerField()

    def __str__(self):
        return f"{self.timestamp} - {self.risk_percentage}% Risk"
    


    
