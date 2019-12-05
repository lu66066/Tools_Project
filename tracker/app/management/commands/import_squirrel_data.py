from django.core.management.base import BaseCommand
from app.models import Sighting

class Command(BaseCommand):
    help = 'import data from path'
    
    def add_arguments(self,parser):
        parser.add_argument('path', type = str)
    
    def handle(self,*args,**kwargs):
        def convert(string):
            if string == 'FALSE':
                return False
            else: return True
        def sp_convert(string):
            if string =='FALSE':
                return 0
            else: return int(string or 0)
        path = kwargs['path']
        import csv
        with open(path) as f:
            reader = csv.reader(f)
            next(reader)
            Sighting.objects.all().delete()
            for row in reader:
                _, created = Sighting.objects.get_or_create(
                 X=float(row[0] or 0),
                 Y=float(row[1] or 0),
                 Unique_Squirrel_ID=row[2],
                 Hectare=row[3],
                 Shift=row[4],
                 Date=row[5],
                 Hectare_Squirrel_Number=int(row[6] or 0),
                 Age=row[7],
                 Primary_Fur_Color=row[8],
                 Highlight_Fur_Color=row[9],
                 Combination=row[10],
                 Color_Notes=row[11],
                 Location=row[12],
                 Above_Ground_Sighter_Measurement=sp_convert(row[13]),
                 Specific_Location=row[14],
                 Running=convert(row[15]),
                 Chasing=convert(row[16]),
                 Climbing=convert(row[17]),
                 Eating=convert(row[18]),
                 Foraging=convert(row[19]),
                 Other_Activities=row[20],
                 Kuks=convert(row[21]),
                 Quaas=convert(row[22]),
                 Moans=convert(row[23]),
                 Tail_Flags=convert(row[24]),
                 Tail_Twitches=convert(row[25]),
                 Approaches=convert(row[26]),
                 Indifferent=convert(row[27]),
                 Runs_From=convert(row[28]),
                 Other_Interactions=row[29]
                )
