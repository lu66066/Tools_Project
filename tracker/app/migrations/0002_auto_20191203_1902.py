# Generated by Django 2.2.7 on 2019-12-03 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='Date',
            field=models.CharField(help_text='Date of the sighting happened', max_length=20),
        ),
    ]
