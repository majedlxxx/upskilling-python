from django.urls import path
from post.views import home_page, create_post
urlpatterns = [
    path('home', home_page),
    path('create', create_post )
]