from django.http import HttpResponse
from django.shortcuts import render

from .models import Pet
# Create your views here.
def  all_squirrel_sightings(request):
    sightings=Sighting.objects.all()
    context={
            'sightings':sightings}
    return render(request, 'app/all.html',context) 
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
