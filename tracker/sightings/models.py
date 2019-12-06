from django.db import models
from django.utils.translation import gettext as _
## Model Creation.
class Sighting(models.Model):
    X = models.FloatField(blank=True,help_text='Using decimal degrees for Longitude.',)
    Y = models.FloatField(blank=True,help_text='Using decimal degrees for Latitude.',)
    Unique_Squirrel_ID = models.CharField(max_length=20,blank=False,help_text='This is a required field.',)
    Hectare = models.CharField(max_length=3,blank=True)
    AM = 'AM'
    PM = 'PM'
    Shift_Choices = (
            (AM,'AM'),
            (PM,'PM'),)
    Shift = models.CharField(max_length=2,choices=Shift_Choices,blank=True,help_text='The shift of the sightinghappened.',)
    Date =  models.DateField(blank=True,help_text='Date of the sighting happened',)
    Hectare_Squirrel_Number = models.IntegerField(blank=True,null=True)
    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    UNKNOWN = '?'
    Age_Choices = (
            (ADULT,'Adult'),
            (JUVENILE,'Juvenlie'),
            (UNKNOWN,'?'),)
    Age = models.CharField(max_length=20,choices=Age_Choices,blank=True,help_text='The age of the squirrel.',)      
    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'
    Primary_Color_Choices = (
            (GRAY,'Gray'),
            (CINNAMON,'Cinnamon'),
            (BLACK,'Black'),)
    Primary_Fur_Color = models.CharField(max_length=20,choices=Primary_Color_Choices,blank=True,help_text='Primary fur color of the squirrel',)
    Highlight_Fur_Color = models.CharField(max_length=50,blank=True)
    Combination = models.CharField(max_length=70,blank=True,)
    Color_Notes = models.CharField(max_length=500,blank=True,)
    GROUND_PLANE = 'Ground Plane'
    ABOVE_GROUND = 'Above Ground'
    Location_Choices = (
            (GROUND_PLANE,'Ground Plane'),
            (ABOVE_GROUND,'Above Ground'),)
    Location = models.CharField(max_length=20,choices=Location_Choices,blank=True,)
    Above_Ground_Sighter_Measurement = models.IntegerField(blank=True,null=True)
    Specific_Location = models.CharField(max_length=500,blank=True)
    Running = models.BooleanField(default=False)
    Chasing = models.BooleanField(default=False)
    Climbing = models.BooleanField(default=False)
    Eating = models.BooleanField(default=False)
    Foraging = models.BooleanField(default=False)
    Other_Activities = models.CharField(max_length=500,blank=True)
    Kuks = models.BooleanField(default=False)
    Quaas = models.BooleanField(default=False)
    Moans = models.BooleanField(default=False)
    Tail_Flags = models.BooleanField(default=False)
    Tail_Twitches = models.BooleanField(default=False)
    Approaches = models.BooleanField(default=False)
    Indifferent = models.BooleanField(default=False)
    Runs_From = models.BooleanField(default=False)
    Other_Interactions = models.CharField(max_length=500,blank=True)

    def __str__(self):
        return self.Unique_Squirrel_ID
# Create your models here.
