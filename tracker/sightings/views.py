from django.http import HttpResponse,HttpResponseRedirect
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
    return render(request, 'sightings/all.html',context) 

def add(request):
    if request.method == 'POST':
        form = SightingForm(request.POST)
        if form.is_valid():
            new_sighting=form.save()
            return HttpResponseRedirect('/sightings/')

    else:
        form=SightingForm()

    context={
            'form':form,
    }

    return render(request,'sightings/add.html',context)

def edit_sighting(request,Unique_Squirrel_ID):
    sighting=Sighting.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
    if request.method == 'POST':
        form = SightingForm(request.POST,instance=sighting)
        if form.is_valid():
            form.save()
            return redirect('/sightings/{Unique_Squirrel_ID}')

    else: 
        form=SightingForm(instance=sighting)

    context={
            'form':form,
    }

    return render(request,'sightings/edit.html',context)

