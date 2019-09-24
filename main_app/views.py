from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Burger


# Imports 
from django.http import HttpResponse

# Defines the home view
def home(request):
    return render(request, 'base.html')    

def about(request): 
    return render(request, 'about.html')

def burgers_detail(request, burger_id):
  burger = Burger.objects.get(id=burger_id)
  return render(request, 'burgers/detail.html', { 'burger': burger })

class BurgerCreate(CreateView):
  model = Burger
  fields = '__all__'
  success_url = '/burgers/'

class BurgerUpdate(UpdateView):
  model = Burger
  fields = ['origin', 'description', 'quality']
  success_url = '/burgers/'

class BurgerDelete(DeleteView):
  model = Burger
  success_url = '/burgers/'

def burgers_index(request):
    burgers = Burger.objects.all()
    return render(request, 'burgers/index.html', { 'burgers': burgers })
