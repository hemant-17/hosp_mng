from django.contrib import admin
from . models import Patient , Doctor,Appointment,Medical,group

# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Medical)
admin.site.register(group)
