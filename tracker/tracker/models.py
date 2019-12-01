from django.db import models
from django.utils.translation import gettext as _
## Model Creation.
class Sighting(models.Model):
    X = models.FloatField(default=None)
    Y = models.FloatField(default=None)
    Unique_Squirrel_ID = models.CharField(max_length = 20,)
    Hectare = models.CharField(max_length = 3,)
    AM = 'AM'
    PM = 'PM'
    Shift_Choices = (
            (AM,'AM'),
            (PM,'PM'),)
    Shift = models.CharField(max_length = 2,choice = Shift_Choices,)
    Date =  models.DateField(help_text = _('Date of the sighting happened'),)
    Hectare_Squirrel_Number = models.IntegerField(min_value = 0, blank = True, null = True)
    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    UNKNOWN = '?'
    Age_Choices = (
            (ADULT,'Adult'),
            (JUVENILE,'Juvenlie'),
            (UNKNOWN,'?'),
            ('Null',''),)
    Age = models.CharField(max_length = 20,choice = Age_Choices,default = 'Null',)       
    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'
    Primary_Color_Choices = (
            (GRAY,'Gray'),
            (CINNAMON,'Cinnamon'),
            (BLACK,'Black'),
            ('Null',''),)
    Primary_Fur_Color = models.CharField(max_length = 20, choice = Primary_Color_Choices, default = 'Null',)
    Highlight_Fur_Color = models.CharField(max_length = 50,)
    Color_Notes = models.CharField(max_length = 500,)
    GROUND_PLANE = 'Ground Plane'
    ABOVE_GROUND = 'Above Ground'
    Location_Choices = (
            (GROUND_PLANE,'Ground Plane'),
            (ABOVE_GROUND,'Above Ground'),
            ('Null',''),)
    Location = models.CharField(max_length = 20, choice = Location_Choices, default = 'Null',)
    Above_Ground_Sighter_Measurement = models.IntegerField(min_value = 0, blank = True, null = True)
    Specific_Location = models.CharField(max_length = 500,)
    Running = models.BooleanField(default = False)
    Chasing = models.BooleanField(default = False)
    Climbing = models.BooleanField(default = False)
    Eating = models.BooleanField(default = False)
    Foraging = models.BooleanField(default = False)
    Other_Activities = models.CharField(max_length = 500,)
    Kuks = models.BooleanField(default = False)
    Quaas = models.BooleanField(default = False)
    Moans = models.BooleanField(default = False)
    Tail_Flags = models.BooleanField(default = False)
    Tail_Twitches = models.BooleanField(default = False)
    Approaches = models.BooleanField(default = False)
    Indifferent = models.BooleanField(default = False)
    Runs_From = models.BooleanField(default = False)
    Other_Interactions - models.CharField(max_length = 500,)
