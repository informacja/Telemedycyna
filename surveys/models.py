from django.db import models

# Create your models here.

class Survey(models.Model):
    sample_text = models.CharField(max_length=1024, blank=True, null=True)
    sample_bool = models.BooleanField(blank=True, null=True, default=False)
    wav_file = models.FileField(upload_to='wav_files', blank=True, null=True)

class Patient(models.Model):
    name_text = models.CharField(max_length=1024, blank=True, null=True)
    pesel_int = models.IntegerField()
    disease_text = models.CharField(max_length=1024, blank=True, null=True)

class Diagnosis(models.Model):
    nameOfPatient_text = models.CharField(max_length=1024, blank=True, null=True)
    diagnosis_text = models.CharField(max_length=1024, blank=True, null=True)






