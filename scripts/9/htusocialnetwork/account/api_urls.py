from django.urls import path
from account.api import login, signup
urlpatterns = [
    path('login', login),
    path('signup',  signup)
]