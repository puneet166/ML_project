# Generated by Django 3.0.4 on 2020-04-07 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0003_diabetes_outcome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diabetes',
            name='BMI',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='diabetes',
            name='DiabetesPedigreeFunction',
            field=models.FloatField(),
        ),
    ]