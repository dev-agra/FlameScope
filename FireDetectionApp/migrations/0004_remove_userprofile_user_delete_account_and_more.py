# Generated by Django 4.1.6 on 2023-03-24 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FireDetectionApp', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
