from django.shortcuts import render, HttpResponse, redirect
from account.models import Account
from account.views import is_logged_in
from post.forms import CreatePost
from post.models import Post
from django.contrib import messages
# Create your views here.

def home_page(request):
    if not is_logged_in(request):
        return redirect('/account/login')
    user = Account.objects.get(username=request.session['username'])
    user_posts = Post.objects.filter(author=user)
    return render(request, 'home.html', context={'create_post_form': CreatePost,
                                                 'posts': user_posts})


def create_post(request):
    if not is_logged_in(request):
        return redirect('/account/login')
    form = CreatePost(request.POST)
    if not form.is_valid():
        messages.error(request, form.errors)
        return redirect('/post/home')
        
    title = form.cleaned_data['title']
    content = form.cleaned_data['content']
    author = Account.objects.get(username=request.session['username'])
    
    new_post = Post(title=title, content=content, author=author)
    new_post.save()
    messages.success(request, 'Created successfully')
    return redirect('/post/home')