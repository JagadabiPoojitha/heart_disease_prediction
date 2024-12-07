from django.contrib import admin
from .models import HealthTip


@admin.register(HealthTip)
class HealthTipAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'description')

# Register your models here.
