from django.shortcuts import render, redirect, HttpResponse
from account.models import Account
from account.forms import SignupForm, LoginForm
from django.contrib import messages
# Create your views here.



def is_logged_in(request):
    return 'username' in request.session




def home(request):
    if is_logged_in(request):
        return redirect('/post/home')
    else:
        return redirect('/account/login')



def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', context={'login_form': LoginForm})
    elif request.method == 'POST':
        #check if username and password are in request.POST
        form = LoginForm(request.POST)
        if not form.is_valid():
            messages.error(request, form.errors)
            redirect('/account/login')
        
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        
        if not Account.objects.filter(username = username).exists():
            messages.error(request, 'wrong username/password')
            return redirect('/account/login')
            
            
        user = Account.objects.get(username=username)
        #if user.password == password # this won't work because the password in the database is hashed.
        if not user.check_password(password):
            messages.error(request, 'wrong username/password')
            return redirect('/account/login')
        
        request.session['username'] = username
        
        return redirect('/post/home')
    else:
        return HttpResponse("Method not allowed")



def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', context={'signup_form': SignupForm})
    elif request.method == 'POST':
        
        form = SignupForm(request.POST)
        if not form.is_valid():
            messages.error(request, form.errors)
            # messages.add_message(request, messages.ERROR, form.errors)
            # messages.error(request, form.errors)
            return redirect('/account/signup')
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        new_account = Account()
        new_account.username = username
        new_account.set_password(password) # we used set password instead of new_account.password = password because set_password hashes the password
        new_account.save()
        messages.success(request, "Created successfully")
        return redirect('/account/login')
        
        
def test_login(request):
    if 'username' not in request.session:
        return HttpResponse("You are not logged in")
    else:
        return HttpResponse(f"You are logged in as {request.session['username']}")
    
def logout(request):
    if 'username' in request.session:
        del request.session['username']
    messages.info(request, "You are logged out")
    return redirect('/account/login')