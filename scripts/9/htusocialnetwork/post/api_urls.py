from django.urls import path
from post.api import get_posts, create_post

urlpatterns = [
    path('get-posts', get_posts),
    path('create-post', create_post)

]