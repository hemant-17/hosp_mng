# Generated by Django 3.0 on 2020-05-21 12:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hosmng', '0013_auto_20200521_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='doc_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctor1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='pat_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient1', to=settings.AUTH_USER_MODEL),
        ),
    ]