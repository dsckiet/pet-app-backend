from django.http.response import JsonResponse
from django.shortcuts import render

def fun(request):
    return JsonResponse("yes" , safe = False)
# Create your views here.
