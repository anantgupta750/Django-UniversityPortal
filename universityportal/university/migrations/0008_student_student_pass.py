# Generated by Django 3.2.9 on 2021-11-28 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0007_rename_registartion_registration'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_pass',
            field=models.CharField(default='', max_length=50),
        ),
    ]