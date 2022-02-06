from django.urls import path
from . import views
urlpatterns=[
    path('',views.home, name="home"),  # Homepage.Can be defined by empty colons or a '/' 
    path('add',views.add,name='add')
]
