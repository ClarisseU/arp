from django import forms
from .models import Trainings, HealthWorker, SymptomsRecord
from tinymce.widgets import TinyMCE


class TrainingForm(forms.ModelForm):
    class Meta:
        model = Trainings
        fields = '__all__'

class HealthWorker(forms.ModelForm):
    class Meta:
        model = HealthWorker
        fields = '__all__'

class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = '__all__'

class SymptomsRecordForm(forms.ModelForm):
    class Meta:
        model = SymptomsRecord
        fields = '__all__'

class update_healthWorkerForm(forms.ModelForm):
    class Meta:
        model = healthWorker
        fields = ("name","password","phonenumber")