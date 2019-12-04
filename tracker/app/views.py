from django.http import HttpResponse
from django.shortcuts import render

from .models import Sighting
# Create your views here.
def  all_squirrel_sightings(request):
    sightings=Sighting.objects.all()
    context={
            'sightings':sightings}
    return render(request, 'app/all.html',context) 
def sighting_details(request,Unique_Squirrel_ID):
    sight=Sighting.objects.get(id=Unique_Squirrel_ID)
    return HttpResponse("Hello, world. You're at the polls index.")
