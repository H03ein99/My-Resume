# Generated by Django 5.1.6 on 2025-02-23 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0007_education_major'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
    ]
