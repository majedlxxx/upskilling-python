from django.shortcuts import render, HttpResponse,  redirect
from account.models import Account

# Create your views here.
def home(request):
    # return HttpResponse("This is home")
    data = {
        'ids': [1,2,3],
        'name': 'majed'
    }
    return render(request, 'home.html', context=data)


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        if Account.objects.filter(fname=username, password=password):
            return HttpResponse("Correct")
        else:
            return HttpResponse("False")
        