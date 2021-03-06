# Generated by Django 3.0.4 on 2020-05-01 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='diabetes',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('Pregnancies', models.IntegerField()),
                ('Glucose', models.IntegerField()),
                ('BloodPressure', models.IntegerField()),
                ('SkinThickness', models.IntegerField()),
                ('Insulin', models.IntegerField()),
                ('BMI', models.FloatField()),
                ('DiabetesPedigreeFunction', models.FloatField()),
                ('Age', models.IntegerField()),
                ('Outcome', models.IntegerField(default=2)),
            ],
        ),
        migrations.CreateModel(
            name='heart',
            fields=[
                ('sno_heart', models.AutoField(primary_key=True, serialize=False)),
                ('age', models.IntegerField()),
                ('sex', models.IntegerField()),
                ('cp', models.IntegerField()),
                ('trestbps', models.IntegerField()),
                ('chol', models.IntegerField()),
                ('fbs', models.IntegerField()),
                ('restecg', models.IntegerField()),
                ('thalach', models.IntegerField()),
                ('exang', models.IntegerField()),
                ('oldpeak', models.FloatField()),
                ('slope', models.IntegerField()),
                ('ca', models.IntegerField()),
                ('thal', models.IntegerField()),
                ('target', models.IntegerField(default=2)),
            ],
        ),
        migrations.CreateModel(
            name='query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Email', models.EmailField(max_length=200)),
                ('Message', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.IntegerField()),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calc.diabetes')),
            ],
        ),
    ]
