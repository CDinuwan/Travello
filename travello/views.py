from django.shortcuts import render
from . models import Destination

# Create your views here.
def index(request):

    dest1=Destination()
    dest1.name='Mumbai'
    dest1.desc="The City That Never Sleep"
    dest1.img='destination_1.jpg'
    dest1.price=700
    dest1.offer=False

    dest2=Destination()
    dest2.name='New York'
    dest2.desc="The City That Never Sleep They think so"
    dest2.img='destination_2.jpg'
    dest2.price=500
    dest2.offer=True

    dest3=Destination()
    dest3.name='England'
    dest3.desc="I think so"
    dest3.img='destination_3.jpg'
    dest3.price=890
    dest3.ofeer=False

    dests=[dest1,dest2,dest3]

    return render(request,'index.html', {'dests': dests})
