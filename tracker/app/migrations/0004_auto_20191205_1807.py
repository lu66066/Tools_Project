# Generated by Django 2.2.7 on 2019-12-05 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_sighting_combination'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='Age',
            field=models.CharField(blank=True, choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenlie'), ('?', '?')], help_text='The age of the squirrel.', max_length=20),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='Color_Notes',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='Combination',
            field=models.CharField(blank=True, max_length=70),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='Date',
            field=models.DateField(blank=True, help_text='Date of the sighting happened'),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='Hectare',
            field=models.CharField(blank=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='Highlight_Fur_Color',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='Location',
            field=models.CharField(blank=True, choices=[('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground')], max_length=20),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='Other_Activities',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='Other_Interactions',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='Primary_Fur_Color',
            field=models.CharField(blank=True, choices=[('Gray', 'Gray'), ('Cinnamon', 'Cinnamon'), ('Black', 'Black')], help_text='Primary fur color of the squirrel', max_length=20),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='Shift',
            field=models.CharField(blank=True, choices=[('AM', 'AM'), ('PM', 'PM')], help_text='The shift of the sightinghappened.', max_length=2),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='Specific_Location',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='Unique_Squirrel_ID',
            field=models.CharField(help_text='This is a required field.', max_length=20),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='X',
            field=models.FloatField(blank=True, help_text='Using decimal degrees for Longitude.'),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='Y',
            field=models.FloatField(blank=True, help_text='Using decimal degrees for Latitude.'),
        ),
    ]