from ast import Return
from django.shortcuts import render

from travello.models import Destinations
# Create your views here.
def index(request):
    dest1 = Destinations()
    dest1.name='Shimla'
    dest1.desc="In the lap of the Himalyas"
    dest1.price=800
    dest2 = Destinations()
    dest2.name='Srinagar'
    dest2.desc="Jannat in the World"
    dest2.price=1500
    dest3 = Destinations()
    dest3.name='Allahabad'
    dest3.desc="Land of culture"
    dest3.price=400
    
    return render(request,"index.html",{'dest1':dest1, 'dest2':dest2, 'dest3':dest3})