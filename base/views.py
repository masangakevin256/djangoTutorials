from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.


rooms=[
    {"id":1, "name":"lets learn python"},
    {"id":2, "name":"lets learn java"},
    {"id":3, "name":"lets learn c++"},
    {"id": 4, "name": "Lets learn react"}
]
def home(request):
    # return HttpResponse("Home Page")
    content = {'rooms': rooms}
    return render(request, 'base/home.html', content)

def room(request):
    # return HttpResponse("Rooms created!")
    return render(request, 'base/room.html')