from django.http.response import JsonResponse
from django.shortcuts import render
from .models import Breed , Category

def get_category(request):
    categories = list(Category.objects.all().values().order_by('category'))
    print(categories)
    return JsonResponse(categories , safe= False , status = 200)

def get_breeds(request):
    category = request.GET['category']
    breeds = list(Breed.objects.filter(category_id = category).values().order_by('breed'))        
    return JsonResponse(breeds , safe= False , status = 200)

