from django.http.response import JsonResponse
from django.shortcuts import render
from .models import BreedInfo , CategoryInfo

def get_category(request):
    categories = list(CategoryInfo.objects.all().values().order_by('category'))
    print(categories)
    return JsonResponse(categories , safe= False , status = 200)

def get_breeds(request):
    category = request.GET['category']
    breeds = list(BreedInfo.objects.filter(category_id = category).values().order_by('breed'))        
    return JsonResponse(breeds , safe= False , status = 200)

