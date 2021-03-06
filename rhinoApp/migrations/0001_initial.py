# Generated by Django 4.0.4 on 2022-05-20 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('residence', models.CharField(max_length=20)),
                ('guardian', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='HealthWorker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('phonenumber', models.IntegerField()),
                ('residence', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Trainings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=800)),
            ],
        ),
        migrations.CreateModel(
            name='SymptomsRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.IntegerField()),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rhinoApp.child')),
            ],
        ),
        migrations.AddField(
            model_name='child',
            name='healthWorker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rhinoApp.healthworker'),
        ),
    ]
