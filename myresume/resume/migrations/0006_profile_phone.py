# Generated by Django 5.1.6 on 2025-02-23 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_profile_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
