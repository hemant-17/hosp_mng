# Generated by Django 3.0 on 2020-05-22 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosmng', '0016_patient_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='status',
            field=models.CharField(blank=True, choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=20, null=True),
        ),
    ]