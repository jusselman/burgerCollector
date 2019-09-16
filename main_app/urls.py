from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('burgers/', views.burgers_index, name='index'),
    path('burgers/<int:burger_id>/', views.burgers_detail, name="detail")
]