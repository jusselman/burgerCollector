from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('burgers/', views.burgers_index, name='index'),
    path('burgers/<int:burger_id>/', views.burgers_detail, name="detail"),
    path('burgers/create/', views.BurgerCreate.as_view(), name="burgers_create"),
    path('burgers/<int:pk>update/', views.BurgerUpdate.as_view(), name="burgers_update"),
    path('burgers/<int:pk>delete/', views.BurgerDelete.as_view(), name="burgers_delete"),
]