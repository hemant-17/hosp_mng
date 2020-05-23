# Generated by Django 3.0 on 2020-05-21 06:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hosmng', '0010_medical_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medical',
            name='doc_name',
        ),
        migrations.RemoveField(
            model_name='medical',
            name='pat_name',
        ),
        migrations.AddField(
            model_name='medical',
            name='docname',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctorto', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='medical',
            name='patname',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patientto', to=settings.AUTH_USER_MODEL),
        ),
    ]