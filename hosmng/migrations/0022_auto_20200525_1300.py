# Generated by Django 3.0 on 2020-05-25 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosmng', '0021_patient_case_paper'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='patient',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]