from django.core.management.base import BaseCommand
from sightings.models import Sighting

class Command(BaseCommand):
        help = 'export data to path'
            
        def add_arguments(self,parser):
            parser.add_argument('path', type = str)
                                
        def handle(self,*args,**kwargs):
            path = kwargs['path']
            field_names = [field.name for field in Sighting._meta.fields]
            import csv
            with open(path, 'w')as csvfile:
                writer = csv.writer(csvfile, delimiter = ' ')
                writer.writerow(field_names)
                for entry in Sighting.objects.all():
                    writer.writerow([getattr(entry,field) for field in field_names])
