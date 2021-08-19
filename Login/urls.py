from django.urls import path, include
from .views import fun

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('profile/' , fun)
]
