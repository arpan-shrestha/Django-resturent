# Generated by Django 2.2.2 on 2020-04-24 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutus',
            name='image',
        ),
    ]
