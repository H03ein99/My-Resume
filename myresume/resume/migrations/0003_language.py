# Generated by Django 5.1.6 on 2025-02-23 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_education_end_date_education_start_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('proficiency', models.CharField(max_length=50)),
            ],
        ),
    ]
