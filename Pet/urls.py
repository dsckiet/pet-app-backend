from django.urls import path, include
from .views import get_breeds , get_category

urlpatterns = [
    path('get_category' , get_category) ,
    path('get_breed/' , get_breeds),
]
