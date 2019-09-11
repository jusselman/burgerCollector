from django.shortcuts import render

# Imports 
from django.http import HttpResponse

# Defines the home view
def home(request):
    return render(request, 'base.html')    
    # return HttpResponse('<h1>(҂`_´)︻╦╤─ ҉</h1>')

def about(request): 
    return render(request, 'about.html')

def burgers_index(request):
    return render(request, 'burgers/index.html', { 'cats': burgers })

class Burger: 
    def __init__(self, name, origin, description, quality):
        self.name = name
        self.origin = origin
        self.description = description
        self.quality = quality

burgers = [
    Burger('FourByFour', 'InNOut', 'Animal styled to perfection', 5),
    Burger('Big Mac', 'MacDonalds', 'Pleasurable for the first 5 minutes', 3),
    Burger('Hang Over', 'Big Mouth', 'It\'s all in the name', 4 ) ,
    Burger('Whopper', 'Burger King', 'Great when they were a dollar', 2)
]