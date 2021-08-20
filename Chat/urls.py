from django.urls import path , re_path

from .views import chat

urlpatterns = [
    re_path(r"^chat/(?P<username>\w+)/$" , chat),
    # path('accounts/', include('Login.urls')),

]
