from django.urls import path
from account.views import login, signup
urlpatterns = [
    path('login', login),
    path('signup', signup)
]