from django.urls import path, include
from .views import fun , my_login , my_logout , register, upload

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('profile/' , fun),#redirect of google and facebook auth
    path('register/' , register),
    path('login/' , my_login),
    path('logout/' , my_logout),
    path('upload/<str:pet_id>/' , upload)
]
