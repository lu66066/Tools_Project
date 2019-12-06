from django.shortcuts import render
from sightings.models import Sighting
import random

def map(request):
    random.seed(0)
    sample_index = random.sample(range(Sighting.objects.count()),100)
    sample_sightings = [Sighting.objects.all()[i] for i in sample_index]
    context = {
        'sample_sightings': sample_sightings,
    }
    return render(request, 'sightings/map.html', context)
# Create your views here.
