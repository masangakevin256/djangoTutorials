from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
from .models import Room

# rooms=[
#     {"id":1, "name":"lets learn python"},
#     {"id":2, "name":"lets learn java"},
#     {"id":3, "name":"lets learn c++"},
#     {"id": 4, "name": "Lets learn react"}
# ]
def home(request):
    rooms = Room.objects.all()
    # return HttpResponse("Home Page")
    content = {'rooms': rooms}
    return render(request, 'base/home.html', content)

def room(request, pk):
    
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    room = Room.objects.get(id=pk)
    context = {"room": room}
    # return HttpResponse("Rooms created!")
    return render(request, 'base/room.html', context)


