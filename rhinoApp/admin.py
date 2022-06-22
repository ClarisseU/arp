from django.contrib import admin
from .models import Trainings, HealthWorker, Child, SymptomsRecord

# Register your models here.
admin.site.register(Trainings)
admin.site.register(HealthWorker)
admin.site.register(Child)
admin.site.register(SymptomsRecord)