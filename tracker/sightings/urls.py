from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns=[
        path('',views.all_squirrel_sightings,name='sighting'),
      #  path('<int:pet_id>/',views.pet_details),
        path('add/', views.add, name='add'),
        path('<Unique_Squirrel_ID>/',views.edit_sighting,name='edit'),
]

