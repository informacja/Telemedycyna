# Generated by Django 3.2.3 on 2022-03-17 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sample_text', models.CharField(blank=True, max_length=1024, null=True)),
                ('sample_bool', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
    ]
