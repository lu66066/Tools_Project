from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Sighting
from .forms import SightingForm
from django.urls import reverse_lazy, reverse

# Create your views here.
def  all_squirrel_sightings(request):
    sightings=Sighting.objects.all()
    context={
            'sightings':sightings}
    return render(request, 'app/all.html',context) 

def sighting_details(request,Unique_Squirrel_ID):
    sight=Sighting.objects.get(id=Unique_Squirrel_ID)
    return HttpResponse("Hello, world. You're at the polls index.")

def edit_sighting(request,Unique_Squirrel_ID):
    sighting=Sighting.objects.get(id=Unique_Squirrel_ID)
    if request.method == 'POST':
        form = SightingForm(request.POST,instance=sighting)
        if form.is_valid():
            form.save()
            return redirect('/app/{Unique_Squirrel_ID}')

    else: 
        form=SightingForm(instance=sighting)

    context={
            'form':form,
    }

    return render(request,'app/edit.html',context)


