from django.contrib import admin
from .models import Doctor,Patient,Appointment

# Register your models here.

class AdminDoctor(admin.ModelAdmin):
    list_display = ['name', 'mobile', 'special']

admin.site.register(Doctor, AdminDoctor)
admin.site.register(Patient)
admin.site.register(Appointment)