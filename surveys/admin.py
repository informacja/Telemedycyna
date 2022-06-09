from django.contrib import admin

from surveys.models import Survey, Patient,Diagnosis

# Register your models here.

@admin.register(Survey)
class SurveytAdmin(admin.ModelAdmin):
    pass

admin.site.register(Patient)
admin.site.register(Diagnosis)