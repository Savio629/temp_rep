from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=255)
    mobile = models.IntegerField()
    special = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    

class Patient(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=25)
    mobile = models.IntegerField()
    address = models.CharField(max_length=255)


    def __str__(self) -> str:
        return self.name
    

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date1 = models.DateField()
    time1 = models.TimeField()

    def __str__(self) -> str:
        return self.doctor.name + " " + self.patient.name
    