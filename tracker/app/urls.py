from django.urls import path

from . import views

urlpatterns=[
        path('sightings/',views.all_squirrel_sightings),
      #  path('<int:pet_id>/',views.pet_details),
]

