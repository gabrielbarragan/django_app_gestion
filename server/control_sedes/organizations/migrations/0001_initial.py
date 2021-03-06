# Generated by Django 4.0.1 on 2022-01-30 18:03

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nit', models.BigIntegerField()),
                ('name', models.CharField(max_length=255)),
                ('comercial_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField(blank=True)),
                ('country', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
