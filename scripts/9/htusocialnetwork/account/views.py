from django.shortcuts import render, redirect
from account.models import Account

# Create your views here.

def login(request):
    return render(request, 'login.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        #Checks
        
        new_account = Account()
        new_account.username = username
        new_account.set_password(password)
        new_account.save()
        return redirect('/account/login')
        