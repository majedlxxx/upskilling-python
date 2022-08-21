from django.urls import path
from account.views import login, signup, test_login, logout
urlpatterns = [
    path('login', login),
    path('signup', signup),
    path('test', test_login),
    path('logout', logout)
]