# Generated by Django 4.0.3 on 2022-06-06 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='date',
        ),
    ]
