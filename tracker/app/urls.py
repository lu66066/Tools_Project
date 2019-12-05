from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns=[
        path('sightings/',views.all_squirrel_sightings,name='sighting'),
      #  path('<int:pet_id>/',views.pet_details),
        path('<int:Unique_Squirrel_ID>/edit/',views.edit_sighting,name='edit'),
]

