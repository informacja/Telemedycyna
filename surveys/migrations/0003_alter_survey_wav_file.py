# Generated by Django 3.2.3 on 2022-05-23 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0002_survey_wav_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='wav_file',
            field=models.FileField(blank=True, db_index=True, null=True, upload_to='wav_files'),
        ),
    ]
