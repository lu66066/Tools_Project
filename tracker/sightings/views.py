from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Sighting
from .forms import SightingForm
from django.urls import reverse_lazy, reverse
from django.db.models import Avg,Max,Min,Count
# Create your views here.
def  all_squirrel_sightings(request):
    sightings=Sighting.objects.all()
    context={
            'sightings':sightings}
    return render(request, 'sightings/all.html',context) 
def stats(request):
    Max_lat=Sighting.objects.aggregate(Max('Y'),Min('Y'),Avg('Y'))
    Max_lon=Sighting.objects.aggregate(Max('X'),Min('X'),Avg('X'))
#    context={
#        'Max_lat':Max_lat,
#    }

    age=Sighting.objects.values('Age').order_by('Age').annotate(age=Count('Age'))
    moans=Sighting.objects.values('Moans').order_by('Moans').annotate(age=Count('Moans'))
    Highlight_Fur_Color=Sighting.objects.values('Highlight_Fur_Color').order_by('Highlight_Fur_Color').annotate(age=Count('Highlight_Fur_Color'))
    context={
            'Max_lat':Max_lat,
            'Max_lon':Max_lon,
            'age':age,
            'moans':moans,
            'Highlight_Fur_Color':Highlight_Fur_Color
    }
    return render(request,'sightings/stats.html',context)

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

