# Generated by Django 4.0.5 on 2022-06-08 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0005_diagnosis_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnosis',
            name='patient2',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='surveys.patient'),
            preserve_default=False,
        ),
    ]
