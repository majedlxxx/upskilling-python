from django.urls import path
from account.views import home, login

urlpatterns = [
    path('', home),
    path('login', login)
]