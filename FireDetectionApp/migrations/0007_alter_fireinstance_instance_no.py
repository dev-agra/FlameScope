# Generated by Django 4.1.6 on 2023-03-24 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FireDetectionApp', '0006_alter_fireinstance_instance_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fireinstance',
            name='instance_no',
            field=models.IntegerField(),
        ),
    ]
