from django.shortcuts import render
from .models import Burger

# Imports 
from django.http import HttpResponse

# Defines the home view
def home(request):
    return render(request, 'base.html')    
    # return HttpResponse('<h1>(҂`_´)︻╦╤─ ҉</h1>')

def about(request): 
    return render(request, 'about.html')

def burgers_detail(request, burger_id):
  burger = Burger.objects.get(id=burger_id)
  return render(request, 'burgers/detail.html', { 'burger': burger })

# class Burger: 
#     def __init__(self, name, origin, description, quality):
#         self.name = name
#         self.origin = origin
#         self.description = description
#         self.quality = quality


def burgers_index(request):
    burgers = Burger.objects.all()
    return render(request, 'burgers/index.html', { 'burgers': burgers })

 # burgers = [
    #     Burger('FourByFour', 'InNOut', 'Animal styled to perfection', 5),
    #     Burger('Big Mac', 'MacDonalds', 'Pleasurable for the first 5 minutes', 3),
    #     Burger('Hang Over', 'Big Mouth', 'It\'s all in the name', 4 ), 
    #     Burger('Whopper', 'Burger King', 'Great when they were a dollar', 2)
    # ]
    # print(burgers)