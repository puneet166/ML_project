# Generated by Django 3.0.4 on 2020-04-12 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0004_auto_20200407_0612'),
    ]

    operations = [
        migrations.CreateModel(
            name='heart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
    ]
