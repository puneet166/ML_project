# Generated by Django 3.0.4 on 2020-05-04 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0009_auto_20200502_0632'),
    ]

    operations = [
        migrations.CreateModel(
            name='role_heart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_heart', models.IntegerField()),
                ('User_id', models.IntegerField()),
            ],
        ),
    ]
