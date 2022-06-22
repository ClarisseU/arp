from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Trainings(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=800)

    def save_trainings(self):
        self.save()

    @classmethod
    def update_trainings(cls, trainings_id, name, description ):
        cls.objects.filter(id = trainings_id).update(name = name, description = description)


class HealthWorker(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    phonenumber = models.IntegerField()
    residence = models.CharField(max_length=20)

    def save_healthWorker(self):
        self.save()

    @classmethod
    def update_healthWorker(cls, healthWorker_id, name, password,phonenumber,residence ):
        cls.objects.filter(id = healthWorker_id).update(name = name, phonenumber = phonenumber, residence=residence )

class Child(models.Model):
    enable_status = (
        ('enabled', 'enabled'),
        ('disabled', 'disabled'),
    )
    
    names = models.CharField(max_length=20)
    age = models.IntegerField()
    residence = models.CharField(max_length=20)
    guardian = models.CharField(max_length=20)
    # status = models.CharField(max_length= 30, enableStatus=enable_status, default='enabled')
    healthWorker = models.ForeignKey(HealthWorker,on_delete=models.CASCADE)

    def save_child(self):
        self.save()

    @classmethod
    def disable_child(cls, id):
        cls.objects.filter(id = id).update(enable_status = 'disabled')

class SymptomsRecord(models.Model):
    facial_status = (
        ('yes', 'yes'),
        ('no' , 'no'),
    )

    cough_status = (
        ('yes', 'yes'),
        ('no', 'no'),
    )
    discharge_status = (
        ('yellow', 'yellow','yellow'),
        ('green', 'green','green'),
        ('None', 'None','None'),
    )
    badBreath_status = (
        ('yes', 'yes'),
        ('no', 'no'),
    )
    diarrhea_status = (
        ('yes', 'yes'),
        ('no', 'no'),
    )
    child = models.ForeignKey(Child,on_delete=models.CASCADE)
    temperature = models.IntegerField()
    # facial_pain = models.CharField(max_length= 30, choices=facial_status, default='yes')
    # cough = models.CharField(max_length= 30, choices=cough_status, default='yes')
    # discharge = models.CharField(max_length= 30, choices=discharge_status, default='yellow')
    # bad_breath = models.CharField(max_length= 30, choices=badBreath_status, default='yes')
    # diarrhea = models.CharField(max_length= 30, choices=diarrhea_status, default='yes')

    def save_symptomsRecord(self):
        self.save()
    

