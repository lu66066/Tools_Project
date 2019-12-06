from django.shortcuts import render
from sightings.models import Sighting
import random

def map(request):
    sample = random.sample(range(Sighting.objects.count()),100)
    sightings = [Sighting.objects.all()[i] for i in sample]
    context = {
        'sightings': sightings,
    }
    return render(request, 'sightings/map.html', context)
# Create your views here.
