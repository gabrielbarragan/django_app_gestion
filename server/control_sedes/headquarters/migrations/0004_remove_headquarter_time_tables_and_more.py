# Generated by Django 4.0.1 on 2022-01-29 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetables', '0001_initial'),
        ('headquarters', '0003_alter_headquarter_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='headquarter',
            name='time_tables',
        ),
        migrations.AddField(
            model_name='headquarter',
            name='time_tables',
            field=models.ManyToManyField(related_name='horarios', to='timetables.TimeTable'),
        ),
    ]
